const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
     devServer: {
         host:"www.devops.cn",
         port: "8080",
     },
})
