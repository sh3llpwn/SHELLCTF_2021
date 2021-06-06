const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');

const app = express();

const PORT = process.env.PORT || 3000;

app.use(cookieParser());

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});

app.get('/', (req, res) => {
    const cookie = req.cookies.flavour;
    if (cookie === 'YWRtaW4=') {
        res.send('SHELL{0NLY_0R30_8e1a91a632ecaf2dd6026c943eb3ed1e}');
        return;
    }
    res.cookie('flavour','dXNlcg==');
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
