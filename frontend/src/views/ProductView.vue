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
                        <a class="button is-dark" @click="addToCart()">
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
import { toast } from 'bulma-toast';

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
        async getProduct() {
            this.$store.commit('setIsLoading, True')

            const product_id = this.$route.params.product_id
            console.log(product_id)
            await axios
            .get(`/api/v1/product/${product_id}/`)
            .then(response => {
                this.product = response.data
                console.log(this.product)
            })
            .catch(error => {
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1){
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 8000,
                position: 'bottom-right',
            })
        }
    }
}
</script>
<style lang="">
    
</style>