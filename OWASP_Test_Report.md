# OWASP Top 10 Security Testing Report

## 1. Reflected XSS Test
- Page: Juice Shop Search Box
- Payload: <script>alert('xss')</script>
- Result: "No results found" displayed; no alert pop-up. Indicates the search box is protected against reflected XSS for this input.

## 2. SQL Injection Test
- Page: Juice Shop Login Form
- Payload: ' OR 1=1 --
- Result: Login success with SQL injection input. Indicates the login form is vulnerable to SQL injection.

## Remediation Recommendations
- **Search Box (XSS):** Sanitize all user inputs before output on web pages.  
- **Login Form (SQLi):** Use parameterized queries or prepared statements to prevent injection.

## References
- https://owasp.org/www-project-juice-shop/  
- https://owasp.org/www-project-top-ten/
