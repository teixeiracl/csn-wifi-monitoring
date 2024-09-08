//import express from 'express';
const express = require('express');
const router = require('./routes/index.ts');

const app = express();
const cors = require('cors');

app.use(cors());
app.use(express.json());
app.use(router);

app.listen(4011, () => console.log('server porta 4011'));
