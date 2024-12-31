# File adapted from https://github.com/langchain-ai/langchain/blob/master/libs/text-splitters/langchain_text_splitters/markdown.py

# MIT License
#
# Copyright (c) LangChain, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Any, NamedTuple, TypedDict


class LineType(TypedDict):
    """Line type as typed dict."""

    metadata: dict[str, str]
    content: str


class HeaderType(TypedDict):
    """Header type as typed dict."""

    level: int
    name: str
    data: str


class Chunk(NamedTuple):
    content: str
    metadata: dict[str, Any]


class MarkdownHeaderTextSplitter:
    """Splitting markdown files based on specified headers."""

    def __init__(
        self,
        headers_to_split_on: list[tuple[str, str]],
        return_each_line: bool = False,
        strip_headers: bool = True,
    ):
        """Create a new MarkdownHeaderTextSplitter.

        Args:
            headers_to_split_on: Headers we want to track
            return_each_line: Return each line w/ associated headers
            strip_headers: Strip split headers from the content of the chunk
        """
        # Output line-by-line or aggregated into chunks w/ common headers
        self.return_each_line = return_each_line
        # Given the headers we want to split on,
        # (e.g., "#, ##, etc") order by length
        self.headers_to_split_on = sorted(
            headers_to_split_on, key=lambda split: len(split[0]), reverse=True
        )
        # Strip headers split headers from the content of the chunk
        self.strip_headers = strip_headers

    def aggregate_lines_to_chunks(self, lines: list[LineType]) -> list[Chunk]:
        """Combine lines with common metadata into chunks
        Args:
            lines: Line of text / associated header metadata
        """
        aggregated_chunks: list[LineType] = []

        for line in lines:
            if (
                aggregated_chunks
                and aggregated_chunks[-1]["metadata"] == line["metadata"]
            ):
                # If the last line in the aggregated list
                # has the same metadata as the current line,
                # append the current content to the last lines's content
                aggregated_chunks[-1]["content"] += "  \n" + line["content"]
            elif (
                aggregated_chunks
                and aggregated_chunks[-1]["metadata"] != line["metadata"]
                # may be issues if other metadata is present
                and len(aggregated_chunks[-1]["metadata"]) < len(line["metadata"])
                and aggregated_chunks[-1]["content"].split("\n")[-1][0] == "#"
                and not self.strip_headers
            ):
                # If the last line in the aggregated list
                # has different metadata as the current line,
                # and has shallower header level than the current line,
                # and the last line is a header,
                # and we are not stripping headers,
                # append the current content to the last line's content
                aggregated_chunks[-1]["content"] += "  \n" + line["content"]
                # and update the last line's metadata
                aggregated_chunks[-1]["metadata"] = line["metadata"]
            else:
                # Otherwise, append the current line to the aggregated list
                aggregated_chunks.append(line)

        return [
            Chunk(content=chunk["content"], metadata=chunk["metadata"])
            for chunk in aggregated_chunks
        ]

    def split_text(self, text: str) -> list[Chunk]:
        """Split markdown file
        Args:
            text: Markdown file"""

        # Split the input text by newline character ("\n").
        lines = text.split("\n")
        # Final output
        lines_with_metadata: list[LineType] = []
        # Content and metadata of the chunk currently being processed
        current_content: list[str] = []
        current_metadata: dict[str, str] = {}
        # Keep track of the nested header structure
        # header_stack: list[dict[str, Union[int, str]]] = []
        header_stack: list[HeaderType] = []
        initial_metadata: dict[str, str] = {}

        in_code_block = False
        opening_fence = ""

        for line in lines:
            stripped_line = line.strip()
            # Remove all non-printable characters from the string, keeping only visible
            # text.
            stripped_line = "".join(filter(str.isprintable, stripped_line))
            if not in_code_block:
                # Exclude inline code spans
                if stripped_line.startswith("```") and stripped_line.count("```") == 1:
                    in_code_block = True
                    opening_fence = "```"
                elif stripped_line.startswith("~~~"):
                    in_code_block = True
                    opening_fence = "~~~"
            else:
                if stripped_line.startswith(opening_fence):
                    in_code_block = False
                    opening_fence = ""

            if in_code_block:
                current_content.append(stripped_line)
                continue

            # Check each line against each of the header types (e.g., #, ##)
            for sep, name in self.headers_to_split_on:
                # Check if line starts with a header that we intend to split on
                if stripped_line.startswith(sep) and (
                    # Header with no text OR header is followed by space
                    # Both are valid conditions that sep is being used a header
                    len(stripped_line) == len(sep) or stripped_line[len(sep)] == " "
                ):
                    # Ensure we are tracking the header as metadata
                    # Get the current header level
                    current_header_level = sep.count("#")

                    # Pop out headers of lower or same level from the stack
                    while (
                        header_stack
                        and header_stack[-1]["level"] >= current_header_level
                    ):
                        # We have encountered a new header
                        # at the same or higher level
                        popped_header = header_stack.pop()
                        # Clear the metadata for the
                        # popped header in initial_metadata
                        if popped_header["name"] in initial_metadata:
                            initial_metadata.pop(popped_header["name"])

                    # Push the current header to the stack
                    header: HeaderType = {
                        "level": current_header_level,
                        "name": name,
                        "data": stripped_line[len(sep) :].strip(),
                    }
                    header_stack.append(header)
                    # Update initial_metadata with the current header
                    initial_metadata[name] = header["data"]

                    # Add the previous line to the lines_with_metadata
                    # only if current_content is not empty
                    if current_content:
                        lines_with_metadata.append(
                            {
                                "content": "\n".join(current_content),
                                "metadata": current_metadata.copy(),
                            }
                        )
                        current_content.clear()

                    if not self.strip_headers:
                        current_content.append(stripped_line)

                    break
            else:
                if stripped_line:
                    current_content.append(stripped_line)
                elif current_content:
                    lines_with_metadata.append(
                        {
                            "content": "\n".join(current_content),
                            "metadata": current_metadata.copy(),
                        }
                    )
                    current_content.clear()

            current_metadata = initial_metadata.copy()

        if current_content:
            lines_with_metadata.append(
                {"content": "\n".join(current_content), "metadata": current_metadata}
            )

        # lines_with_metadata has each line with associated header metadata
        # aggregate these into chunks based on common metadata
        if not self.return_each_line:
            return self.aggregate_lines_to_chunks(lines_with_metadata)
        else:
            return [
                Chunk(content=chunk["content"], metadata=chunk["metadata"])
                for chunk in lines_with_metadata
            ]
