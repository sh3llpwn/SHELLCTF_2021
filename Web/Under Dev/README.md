# UNDER Development

## Description

This is a simple cookie-changing web challenge.

## Solution
1. index.html tells us that the site has no proper auth and a hint about cookies.
2. On checking the coockies the website uses, there is one "privilege" set to base64 value of "user.
3. You just need to change the cookie value to the base64 value of "admin".

The flag is:

```
SHELL{0NLY_0R30_8e1a91a632ecaf2dd6026c943eb3ed1e}
```
