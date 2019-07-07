import requests

# This URL will be the URL that your login form points to with the "action"
# tag.
POSTLOGINURL = 'https://splunged.com/users/signin'

# This URL is the page you actually want to pull down with requests.
REQUESTURL = 'https://splunged.com/'


# username-input-name is the "name" tag associated with the username input field of the login form.
# password-input-name is the "name" tag associated with the password input field of the login form.
payload = {
    'username': 'Maven',
    # Preferably set your password in an env variable and sub it in.
    'password': 'fypmnov14'
}

with requests.Session() as session:
    post = session.post(POSTLOGINURL, data=payload)
    r = session.get(REQUESTURL)
    print(post.text)


# TODO Use with flask to create a web page/app to run from my server
# TODO Find a way to stream the post data and only user name + comment
