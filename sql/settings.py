server = 'servername.database.windows.net'
database = 'database1'
username = 'azureuser'
password = '@verycoolsecurepassw0rd'   
driver= '{ODBC Driver 17 for SQL Server}'

# Make sure you installed ODBC driver of MS
# FOR MAC
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
# brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
# brew update
# HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools