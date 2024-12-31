import base64
from pathlib import Path
from .base import ModuleTestBase


class TestExtractous(ModuleTestBase):
    targets = ["http://127.0.0.1:8888"]
    modules_overrides = ["extractous", "filedownload", "httpx", "excavate", "speculate"]
    config_overrides = {"web": {"spider_distance": 2, "spider_depth": 2}}

    pdf_data = base64.b64decode(
        "JVBERi0xLjMKJe+/ve+/ve+/ve+/vSBSZXBvcnRMYWIgR2VuZXJhdGVkIFBERiBkb2N1bWVudCBodHRwOi8vd3d3LnJlcG9ydGxhYi5jb20KMSAwIG9iago8PAovRjEgMiAwIFIKPj4KZW5kb2JqCjIgMCBvYmoKPDwKL0Jhc2VGb250IC9IZWx2ZXRpY2EgL0VuY29kaW5nIC9XaW5BbnNpRW5jb2RpbmcgL05hbWUgL0YxIC9TdWJ0eXBlIC9UeXBlMSAvVHlwZSAvRm9udAo+PgplbmRvYmoKMyAwIG9iago8PAovQ29udGVudHMgNyAwIFIgL01lZGlhQm94IFsgMCAwIDU5NS4yNzU2IDg0MS44ODk4IF0gL1BhcmVudCA2IDAgUiAvUmVzb3VyY2VzIDw8Ci9Gb250IDEgMCBSIC9Qcm9jU2V0IFsgL1BERiAvVGV4dCAvSW1hZ2VCIC9JbWFnZUMgL0ltYWdlSSBdCj4+IC9Sb3RhdGUgMCAvVHJhbnMgPDwKCj4+IAogIC9UeXBlIC9QYWdlCj4+CmVuZG9iago0IDAgb2JqCjw8Ci9QYWdlTW9kZSAvVXNlTm9uZSAvUGFnZXMgNiAwIFIgL1R5cGUgL0NhdGFsb2cKPj4KZW5kb2JqCjUgMCBvYmoKPDwKL0F1dGhvciAoYW5vbnltb3VzKSAvQ3JlYXRpb25EYXRlIChEOjIwMjQwNjAzMTg1ODE2KzAwJzAwJykgL0NyZWF0b3IgKFJlcG9ydExhYiBQREYgTGlicmFyeSAtIHd3dy5yZXBvcnRsYWIuY29tKSAvS2V5d29yZHMgKCkgL01vZERhdGUgKEQ6MjAyNDA2MDMxODU4MTYrMDAnMDAnKSAvUHJvZHVjZXIgKFJlcG9ydExhYiBQREYgTGlicmFyeSAtIHd3dy5yZXBvcnRsYWIuY29tKSAKICAvU3ViamVjdCAodW5zcGVjaWZpZWQpIC9UaXRsZSAodW50aXRsZWQpIC9UcmFwcGVkIC9GYWxzZQo+PgplbmRvYmoKNiAwIG9iago8PAovQ291bnQgMSAvS2lkcyBbIDMgMCBSIF0gL1R5cGUgL1BhZ2VzCj4+CmVuZG9iago3IDAgb2JqCjw8Ci9GaWx0ZXIgWyAvQVNDSUk4NURlY29kZSAvRmxhdGVEZWNvZGUgXSAvTGVuZ3RoIDEwNwo+PgpzdHJlYW0KR2FwUWgwRT1GLDBVXEgzVFxwTllUXlFLaz90Yz5JUCw7VyNVMV4yM2loUEVNXz9DVzRLSVNpOTBNakdeMixGUyM8UkM1K2MsbilaOyRiSyRiIjVJWzwhXlREI2dpXSY9NVgsWzVAWUBWfj5lbmRzdHJlYW0KZW5kb2JqCnhyZWYKMCA4CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDA3MyAwMDAwMCBuIAowMDAwMDAwMTA0IDAwMDAwIG4gCjAwMDAwMDAyMTEgMDAwMDAgbiAKMDAwMDAwMDQxNCAwMDAwMCBuIAowMDAwMDAwNDgyIDAwMDAwIG4gCjAwMDAwMDA3NzggMDAwMDAgbiAKMDAwMDAwMDgzNyAwMDAwMCBuIAp0cmFpbGVyCjw8Ci9JRCAKWzw4MGQ5ZjViOTY0ZmM5OTI4NDUwMWRlYjdhNmE2MzdmNz48ODBkOWY1Yjk2NGZjOTkyODQ1MDFkZWI3YTZhNjM3Zjc+XQolIFJlcG9ydExhYiBnZW5lcmF0ZWQgUERGIGRvY3VtZW50IC0tIGRpZ2VzdCAoaHR0cDovL3d3dy5yZXBvcnRsYWIuY29tKQoKL0luZm8gNSAwIFIKL1Jvb3QgNCAwIFIKL1NpemUgOAo+PgpzdGFydHhyZWYKMTAzNAolJUVPRg=="
    )

    docx_data = base64.b64decode(
        "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"
    )

    expected_result_pdf = "Hello, World!"
    expected_result_docx = "Hello, World!!"

    async def setup_after_prep(self, module_test):
        module_test.set_expect_requests(
            {"uri": "/"},
            {"response_data": '<a href="/Test_PDF"/><a href="/Test_DOCX"/>'},
        )
        module_test.set_expect_requests(
            {"uri": "/Test_PDF"},
            {"response_data": self.pdf_data, "headers": {"Content-Type": "application/pdf"}},
        )
        module_test.set_expect_requests(
            {"uri": "/Test_DOCX"},
            {
                "response_data": self.docx_data,
                "headers": {"Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"},
            },
        )

    def check(self, module_test, events):
        filesystem_events = [e for e in events if e.type == "FILESYSTEM"]
        assert 2 == len(filesystem_events), filesystem_events
        for filesystem_event in filesystem_events:
            file = Path(filesystem_event.data["path"])
            assert file.is_file(), "Destination file doesn't exist"
            assert (
                open(file, "rb").read() == self.pdf_data or open(file, "rb").read() == self.docx_data
            ), f"File at {file} does not contain the correct content"
        raw_text_events = [e for e in events if e.type == "RAW_TEXT"]
        assert 2 == len(raw_text_events), "Failed to emit RAW_TEXT event"
        for raw_text_event in raw_text_events:
            assert raw_text_event.data in [
                self.expected_result_pdf,
                self.expected_result_docx,
            ], f"Text extracted from {raw_text_event.data['path']} is incorrect, got {raw_text_event.data}"
