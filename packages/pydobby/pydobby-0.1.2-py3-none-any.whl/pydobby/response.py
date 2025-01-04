class HTTPResponse:
    STATUS_CODES = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
    }

    def __init__(
        self,
        status_code=200,
        body: str | bytes = "",
        headers: dict = None,
        content_type: str = "text/plain",
    ):
        self._validate_status_code(status_code)
        self.status_code = status_code
        self.status_text = self.STATUS_CODES.get(status_code, "temp")
        self.content_type = content_type
        self.headers = headers or {}
        self.body = self._prepare_body(body)
        self.headers = headers or {}
        self._set_headers(content_type)

    def _set_headers(self, content_type: str):
        if self.body:
            self._set_content_type(content_type)
            self._set_content_length()

    def _set_content_type(self, content_type: str):
        if "Content-Type" not in self.headers:
            self.headers["Content-Type"] = content_type
        elif self.headers["Content-Type"] != content_type:
            raise ValueError("Content-Type header must match the content_type argument")

    def _set_content_length(self):
        self.headers["Content-Length"] = str(len(self.body))

    def _prepare_body(self, body: str | bytes):
        if body == "" or body is None:
            return b""

        # handle both string and bytes
        if isinstance(body, str):
            return body.encode("utf-8")
        elif isinstance(body, bytes):
            return body
        else:
            raise ValueError("Body must be either a string or bytes")

    def _validate_status_code(self, status_code: int):
        try:
            self.status_code = int(status_code)
        except (ValueError, TypeError):
            raise TypeError("HTTP status code must be an integer.")

        if not 100 <= status_code <= 599:
            raise ValueError("status code must be between 100 and 599")

    def to_bytes(self):
        response = f"HTTP/1.1 {self.status_code} {self.status_text}\r\n"
        if self.headers:
            for header, value in self.headers.items():
                response += f"{header}: {value}\r\n"
        response += "\r\n"
        headers = response.encode("utf-8")
        return headers + self.body

    def set_cookie(
        self,
        name,
        value,
        max_age=None,
        expires=None,
        path="/",
        domain=None,
        secure=False,
        httponly=False,
        samesite="Lax",
    ):
        attributes = {
            "Max-Age": max_age,
            "Expires": expires,
            "Path": path,
            "Domain": domain,
            "Secure": secure,
            "HttpOnly": httponly,
            "SameSite": samesite,
        }

        cookie = [f"{name}={value}"]

        for key, val in attributes.items():
            if isinstance(val, bool):
                if val:
                    cookie.append(key)
            elif val is not None:
                cookie.append(f"{key}={val}")

        self.headers["Set-Cookie"] = "; ".join(cookie)
