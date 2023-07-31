<template lang="en">
    <div class="page-search">
        <div class="is-12">
            <h1 class="title">Search</h1>
            <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
        </div>
        <div class="columns is-multiline">
            
            <div class="column product is-2" v-for="product in products" v-bind:key="product.id">
                <div class="box">
                <figure class="image mb-4">
                    <img :src="product.get_thumbnail" class="image__img" alt="thumbnail">
                </figure>

                <h3 class="is-size-4">{{ product.name }}</h3>
                <p class="is-size-6 has-text-grey">${{ product.price }}</p>

                <router-link :to="'/product/' + product.id">View</router-link>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';


export default {
    name: 'SearchView',
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')
            
            this.perfromSearch()
        }
    },
    methods: {
        async perfromSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('api/v1/product/search/', {'query': this.query})
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            
                this.$store.commit('setIsLoading', false)
                
        }
    }
}
</script>
<style lang="">
    
</style>