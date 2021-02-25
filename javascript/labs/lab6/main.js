let app = new Vue({
    el: '#app',
    data: {
        cat_url: "",
        categories: [],
        selectedCategory: ""
    },
    methods: {
        getImage: async function() {
            const response = await axios({
                url: "https://api.thecatapi.com/v1/images/search",
                method: 'get',
                params: {
                    category_ids: this.selectedCategory
                }
            })
            console.log(response.data)
            this.cat_url = response.data[0].url
            // console.log(this.cat_url)
        }
    },
    created: async function() {
        let response = await axios({
            method: 'get',
            url: "https://api.thecatapi.com/v1/categories"
        })
        // console.log(response.data)
        this.categories = response.data
    }
})