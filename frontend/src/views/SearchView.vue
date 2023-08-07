<template lang="en">
    <h1 class="search-query">Товары по запросу "{{ query }}"</h1>

    <div class="search-wrapper">

        <div class="product-card" v-for="product in products" v-bind:key="product.id">
            <router-link class="product-card__link" :to="'/product/' + product.id">
                <div class="product-card__image-container">
                <img class="product-card__image" :src="product.get_thumbnail" alt="product">
                </div>
                <p class="product-card__title">
                {{ product.name }}
                </p>
                <p class="product-card__specs"><span v-for="(value, key, index) in product.specs" :key="index">{{  value  }}, </span></p>
                <div class="product-card__wrapper">
                <div class="product-card__price-wrapper">
                    <p class="product-card__price-old">$19999</p>
                    <p class="product-card__price">${{ product.price }}</p>
                </div>
                <div class="product-card__button-wrapper">
                    <a class="product-card__buy-button" href="#">
                    <img class="product-card__buy-image" src="@/assets/img/buy-button.svg" alt="buy-button">
                    </a>
                </div>
                </div>
            </router-link>
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
<style lang="scss">
    .search-query {
        font-size: 28px;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
    }
    .search-wrapper {
    display: flex;
    padding-top: 50px;
    gap: 60px;
    justify-content: center;
    flex-wrap: wrap;
}
</style>