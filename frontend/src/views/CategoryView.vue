<template lang="en">
    <h1 class="category-wrapper__title">{{ categoryName }}</h1>
    <div class="category-wrapper">
        
        <div class="product-card" v-for="product in products" v-bind:key="product.id">
            <router-link class="product-card__link" :to="'/product/' + product.id">
                <div class="product-card__image-container">
                <img class="product-card__image" :src="product.get_thumbnail" alt="product">
                </div>
                <p class="product-card__title">
                {{ product.name }}
                </p>
                <p class="product-card__specs">Lorem ipsum dolor sit amet cdddddddddddonsectetur adipisicing elit. Ullam nostrum itaque enim aliquid aut, nu. Ullam nostrum itaque enim aliquid aut, nulla placeat eligendi . Ullam nostrum itaque enim aliquid aut, nulla placeat eligendi . Ullam nostrum itaque enim aliquid aut, nulla placeat eligendi lla placeat eligendi culpa. Ducimus, officiis.</p>
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
    name: "ComponentView",
    data() {
        return {
            products: [],
            categoryName: ''
        }
    },
    mounted() {
        this.getProductsByCategory()
    },
    methods: {
        async getProductsByCategory() {
            await axios
                .post('/api/v1/product/category/', {
                    'category': this.$route.params.category_id,
                })
                .then(response => {
                    console.log(response)
                    this.products = response.data
                    this.categoryName = response.data[0].category.name
                    
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
<style lang="scss">
.category-wrapper {
    display: flex;
    padding-top: 50px;
    gap: 60px;
    justify-content: center;
    flex-wrap: wrap;

    &__title {
        font-size: 28px;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
    }
}
</style>