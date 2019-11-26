# Aplikacja Lekarz (nazwa robocza)

## How to install
1. Download repo, 
2. Initialize virtual environment in it: `python -m venv env`,
3. Run that venv: 
  * Linux: `source env/bin/activate`
  * Windows: `env/Scripts/activate`
4. Install dependencies: `pip install -r requirements.txt`,
5. Install frontend dependencies: `npm install`
6. Compile frontend assets: `npm run dev`,
7. (optional) Change database settings in settings.py if you want to use different (non-sqlite) db backend, 
8. Migrate database: `python manage.py migrate`,
9. To run dev server: `python manage.py runserver`

## Tips for devs

### Dumping pip installations into the file
If you installed new pip dependency you need to allow others to know about it. To do so it is best to save all requirements
in one file, which in this case in named `requirements.txt`. You can do this by typing following command: 

`pip freeze > requirements.txt`

### Authorization with token:
1. `python manage.py runserver`
2. `http://localhost:8000/o/applications/`
3. Chose name
4. Edit client id and client secret (write something easy to copy)
5. Client type : Confidential
6. Authorization grant type: Authorization Code
7. Redirect uris: for example: `http://example.com/`
8. `http://localhost:8000/o/authorize?response_type=code&client_id=<client_id>&redirect_uri=http://example.com/`
9. Copy code, which will show in link, for example: `http://example.com/?code=t5Qw6WkLxoSHDzbz3ZMug149c17L8a`
10.From Linux consol `curl -X POST -d "grant_type=authorization_code&code=<your_code>&redirect_uri=http://example.com/" "http://<client_id>:<client_secret>@localhost:8000/o/token/" `
10b. If you get `{"error": "invalid_grant"}` go `http://localhost:8000/admin/` ->Grants -> edit -> Select your grant -> edit -> Change expires time
11. You will get something like: {"access_token": "1h3GxfFwapKuxnLKWDPoa1xHjiPCJS", "expires_in": 36000, "token_type": "Bearer", "scope": "read write", "refresh_token": "BqlwjJSOj34bYST4mvjUzfnzYtHwmr"}
12. `curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/hello/`
13. You should get: Hello, OAuth2!
14. Next time you can use `curl --data "token=<refresh_token>&client_id=<client_id>&client_secret=<client_secret>" http://localhost:8000/o/revoke_token/` to revoke_token, when it expires (or modify in admin panel)

