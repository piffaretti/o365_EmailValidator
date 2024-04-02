# o365_EmailValidator

O365_emailvalidator is a script to validate if an e-mail exists (is valid) or not in the Microsoft 365.

It employs a technique that queries the URL: https://tenantname-my.sharepoint.com/personal/<your user name>/_layouts/15/onedrive.aspx.

The best part? It remains undetectable by the blue team and there is no blocking or rate limit by MS! 😎

You need the Tenant name, major part is companyname+corp or companyname+country code or just company name. You can try search oin google:

"Companyname" site:sharepoint.com

Example: Company name is CrazyPiffaretti and is located in Switzerland
Porbabily names of tenant:
Crazypiffaretticorp
Crazypiffaretti
Crazypiffarettich (ch is the code of switzerland)
