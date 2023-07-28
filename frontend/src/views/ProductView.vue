<template lang="">
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img :src="product.image" alt="product_image">
                </figure>
                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>
            </div>
            <div class="column is-3">
                <h2 class="subtitle">
                    information
                </h2>
                <p><strong>Price:</strong>{{product.price}}</p>
                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>
                    <div class="control">
                        <a href="" class="button is-dark">
                            Add to cart
                        </a>
                    </div>
                </div>
            </div>
        </div>

        
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'ProductView',
    data() {
        return {
            product: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        getProduct() {
            const product_id = this.$route.params.product_id
            console.log(product_id)
            axios
            .get(`/api/v1/product/${product_id}/`)
            .then(response => {
                this.product = response.data
                console.log(this.product)
            })
            .catch(error => {
                console.log(error)
        })
        }
    }
}
</script>
<style lang="">
    
</style>