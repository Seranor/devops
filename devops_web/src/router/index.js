import {createRouter, createWebHistory} from 'vue-router'
import ShowCenter from '../views/ShowCenter.vue'
import Login from '../views/Login.vue'
import Base from '../views/Base'
import Host from '../views/Host'
import Console from '../views/Console'
import MultiExec from '../views/MultiExec'
import Environment from '../views/Environment'
import Release from '../views/Release'
import Git from '../views/Git'
import Jenkins from '../views/Jenkins'
import Schedule from "../views/Schedule"
import Monitor from "../views/Monitor"
import store from "../store"

const routes = [
    {
        meta: {
            title: 'devops运维',
            authenticate: true,
        },
        path: '/devops',
        alias: '/', // 给当前路径起一个别名
        name: 'Base',
        component: Base, // 快捷键：Alt+Enter快速导包
        children: [
            {
                meta: {
                    title: '展示中心',
                    authenticate: true,
                },
                path: 'show_center',
                alias: '',
                name: 'ShowCenter',
                component: ShowCenter
            },
            {
                meta: {
                    title: '资产管理',
                    authenticate: true,
                },
                path: 'host',
                name: 'Host',
                component: Host
            },
            {
                meta: {
                    title: 'Console',
                    authenticate: true,
                },
                path: 'console/:host_id',
                name: 'Console',
                component: Console
            },
            {
                meta: {
                    title: '批量命令',
                    authenticate: true,
                },
                path: 'multi_exec',
                name: 'MultiExec',
                component: MultiExec,
            },
            {
                meta: {
                    title: '环境管理',
                    authenticate: true,
                },
                path: 'environment',
                name: 'Environment',
                component: Environment,
            },
            {
                meta: {
                    title: '应用管理',
                    authenticate: true,
                },
                path: 'release',
                name: 'Release',
                component: Release,
            },
            {
                meta: {
                    title: 'Git仓库管理',
                    authenticate: true,
                },
                path: 'git',
                name: 'Git',
                component: Git,
            },
            {
                meta: {
                    title: 'Jenkins构建',
                    authenticate: true,
                },
                path: 'jenkins',
                name: 'Jenkins',
                component: Jenkins,
            },
            {
                meta: {
                    title: '定时任务',
                    authenticate: true,
                },
                path: 'schedule',
                name: 'Schedule',
                component: Schedule,
            },
            {
                meta: {
                    title: '监控信息',
                    authenticate: true,
                },
                path: 'monitor',
                name: 'Monitor',
                component: Monitor,
            }
        ]
    },


    {
        meta: {
            title: '账户登陆',
            authenticate: false,
        },
        path: '/login',
        name: 'Login',
        component: Login // 快捷键：Alt+Enter快速导包
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    // console.log("to", to)
    // console.log("from", from)
    // console.log("store.getters.token:", store.getters.token)
    if (to.meta.authenticate && store.getters.token === "") {
        next({name: "Login"})
    } else {
        next()
    }
});

export default router

