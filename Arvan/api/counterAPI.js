const events = require('events')
const eventEmitter = new events.EventEmitter()

const Server = require('semicolon-server')
const Router = require('semicolon-router')
const Redis = require('ioredis')


const { serverRequirement } = require('./config')

const server = new Server(serverRequirement, eventEmitter)
const router = new Router(eventEmitter)
const redis = new Redis()

// Database
async function getAllNumbers() {
    let result = {}
    try {
        const keys = await redis.keys('*');
        const values = await redis.mget(keys);
        for (let i = 0; i < keys.length; i++) {
            result[keys[i]]=parseInt(values[i])  
        }
        return result
    } catch (error) {
        console.error(error);
        return false
    }
}

async function getCount(num) {
    const key = num;
    try {
        const result = await redis.get(key);
        return result
    } catch (error) {
        console.error(error);
        return false
    }
}

async function setNumber(num) {
    try {
        await redis.set(num, 0);
    } catch (error) {
        console.error(error);
    }
}

async function increamentCounter(num) {
    const key = num;
    try {
        const points = await redis.incr(key);
    } catch (error) {
        console.error(error);
    }
}

// Response
ok = (response, data) => {
    response.statusCode = 200
    response.writeHead(200, { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' })
    response.write(JSON.stringify(data))
    response.end('')
}

errorServerInternal = (response, data) => {
    response.statusCode = 500
    response.writeHead(500, { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' })
    response.write(JSON.stringify(data))
    response.end('')
}


// Controller
appRoutes = [{
    url: '/',
    method: 'GET',
    handler:     getSTH = async (request, response) => {
        let state = {}
        let data
        try {
            result = getCount(request.headers['client-key'])
            if (result == false || result == 0) {
                counter = 0
                setNumber(request.headers['client-key'])
            }
            increamentCounter(request.headers['client-key'])
            getCount(request.headers['client-key'])
            state = await getAllNumbers()
            data = {'state':  state }
            ok(response, data)

        } catch (err) {
            errorServerInternal(response, err)
        }
    },
    middlewares: []
}]


// App
server.start()
router.app(appRoutes)