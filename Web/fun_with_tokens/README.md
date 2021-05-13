# Fun With Tokens

## Description

This challenge is based on Path Traversal and JWTs.

## Exploit

1. In the website source, you can see that there's a route to login (`/login`) and a route to get the names of the admins (`/adminNames`). 
2. Get admin names by visiting /adminNames, Lets try to use on of the names to login.
3. So, when you try to visit `/login`, you see a form. Post that along with username of one admin and check the response on the Network Tab in your browser. You can see there's a header called `token` which stores a JWT. You can decode the token (maybe on [jwt.io](https://jwt.io)) to see that the payload is of this format (I typed username:din_djarin11, password: abc):

```
{
  "username": "qva_qwneva11",
  "password": "nop",
  "admin": "snyfr",
  "iat": 1620893711
}
```

4. We can see that the `username` changed from `din_djarin11` to `qva_qwneva11`. So this hints that this could be `rot13`. When you apply the `rot13` cipher on the admin value `snyfr`, you see that it returns a string `false`. So, we can change this to a rot13 encrypted string for `true`, but to do that, we need the JWT secret, to sign the newly created json web token.

5. If you observe the request on `/adminNames`, you see that it actally redirects to `/getFile?file=admins`. This route seems suspicious. We can try to include other files using this. When you try `/getFile?file=.env`, it returns `No such file or directory: /app/public/.env`. So, we can try `../.env` to come out of the public folder. You get a file in return, which is the `.env` containing the secret!

```
JWT_SECRET=G00D_s0ld13rs_k33p_s3cret5
```

6. Use this secret to create a new token. Change value of admin to 'gehr' (rot13 of true). In jwt.io, input the secret in box which says your-256bit-secret. Voila you have a newly created JWT that can get you admin privileges.
Now, visit the `/admin` route. It says:

```
{
"success":false,
"message":"Maybe send the token via Headers ... for Authorization?"
}
```

Which means, you'll have to pass the JWT in the headers. Auth tokens are generally passed in the Authorization header, the message is a hint of that. When you pass the new formed JWT in the Authorization header. You can do this using Burpsuite. 
Intercept the request in proxy tab, and in the request text add 1 line :
```
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InF2YV9xd25ldmExMSIsInBhc3N3b3JkIjoibm9wIiwiYWRtaW4iOiJnZWhyIiwiaWF0IjoxNjIwODk0MjE2fQ.uCl-PVmHPsqz07KTZWn-rSblRdagIw-HgHegOY8p-7U
```

Forward that request.
The text in the response in browser is:

```
Hey din_djarin11! Here's your flag: FURYY{G0x3af_q0_z4gg3e_4r91ns4506s384q460s0s0p6r9r5sr4n}
```

rot13 decrypt this flag to get the real flag.

The flag is:
```
SHELL{T0k3ns_d0_m4tt3r_4e91af4506f384d460f0f0c6e9e5fe4a}
```
