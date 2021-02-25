
let app = new Vue({
    el: '#app',
    data: {
        passwordLength: "",
        password: "",
        result: "",
        char: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    },
    methods: {
        genPassword: function() {
            let counter = 0
            this.password = ''
            while (counter < parseInt(this.passwordLength)) {
                let randChar = this.char[Math.floor(Math.random()*this.char.length)]
                this.password += randChar
                counter++
            }
            this.passwordLength = ''
            return this.password
        },
        message: function() {
            this.password = this.genPassword()
            this.result = `Your password is ${this.password}`
        }
    }
})