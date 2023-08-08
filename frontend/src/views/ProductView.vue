<template lang="en">
    <!-- <div class="page-product">
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

        
    </div> -->

    <div class="product-page">
        <h1 class="product-page__title">{{ product.name }}</h1>
        
        <div class="product-page__card-wrapper">
            <div class="product-page__image-wrapper">
                <img class="product-page__image" :src="product.image" alt="image">
            </div>
            <div class="product-page__specs-wrapper">
                <img src="@/assets/img/rating.svg" alt="rating" class="product-page__rating">
                <div class="product-page__feature feature" v-for="(value, key, index) in product.specs" v-bind:key="index">
                    <p class="feature__key"><strong>{{ key }}: </strong><span class="feature__value">{{ value }}</span></p>
                </div>
            </div>
            <div class="product-page__price-wrapper">
                <p class="product-page__price-old">19999</p>
                <p class="product-page__price">{{ product.price }}</p>
                <a href="#" @click="addToCart()">
                    <img class="product-page__send-to-cart-button" src="@/assets/img/to-cart-button.jpg" alt="to-cart-button">
                </a>
            </div>
        </div>

        <div class="specs">
            <h2 class="specs__title">Полная характеристика</h2>
            <div class="product-page__feature feature" v-for="(value, key, index) in product.specs" v-bind:key="index">
                <p class="feature__key"><strong>{{ key }}: </strong><span class="feature__value">{{ value }}</span></p>
                <hr>
            </div>
        </div>
        <div class="description">
            <h3 class="description__title">
                Описание
            </h3>
            <p class="description__text">{{ product.description }}</p>
        </div>
        <div class="reviews">
            <h4 class="reviews__title">
                Отзывы
            </h4>
            <div class="reviews__list" v-if="Object.keys(reviews).length != 0 ">
                <div class="reviews__review-wrapper" v-for="review in reviews" v-bind:key="review.id" >
                    <div class="reviews__username-wrapper">
                        <img src="@/assets/img/user.svg" alt="icon" class="reviews__icon" width="50">
                        
                        <p class="reviews__username">{{ review.owner.username}}</p>
                        <p class="review__rating">Оценка: {{ review.rating }}</p>
                    </div>
                    <p class="reviews__text">
                        {{ review.text }}
                    </p>
                </div>
            </div>
            <p v-else>Отзывы отсутствуют.</p>
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
            reviews: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct()
        this.getReviews()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

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
        async getReviews() {
            const product_id = this.$route.params.product_id
            await axios 
                .get(`/api/v1/review/${product_id}/`)
                .then(response => {
                    this.reviews = response.data.results
                    console.log(this.reviews)
                })
                .catch(error => {
                    console.log(error)
                })
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
<style lang="scss">
    strong {
        font-weight: 700;
    }
    .product-page {
        background-color: white;
        box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.2);
        border-radius: 5px;
        padding: 30px;
        padding-left: 80px;
        margin-top: 30px;

        .feature {
            margin: 15px 0;
            font-size: 16px;
            letter-spacing: 1px;
            max-width: 400px;
            word-wrap: break-word;
        }
        &__card-wrapper {
            display: flex;
            flex-wrap: wrap;
        }
        &__title{
            font-size: 30px;
            font-weight: 700;
            // text-align: center;
            // margin-top: 20px;
            margin-bottom: 10px;
            color: #151528;
            letter-spacing: 0.1px;

            
        }
        &__price-old {
            text-decoration: line-through;
            font-size: 24px;
        }
        &__send-to-cart-button{
            margin-top: 30px;
            width: 150px;
        }
        &__price {
            font-size: 32px;
            font-weight: 700;
        }
        &__price-wrapper {
            // max-width: 400px;
            margin: auto 0;
            margin-left: 50px;

        }
        &__image{
                max-width: 450px;
                height: 400px;
                object-fit: contain;
            }
        &__specs-wrapper {
            // display: flex;
            flex-direction: column;
            align-items: center;
            margin: auto 0;

            margin-left: 120px;
            margin-right: 100px;
        }
        .specs {
            &__title {
                font-size: 24px;
                font-weight: 700;
            }
        }
        .description {
            margin: 30px 0;
            &__title {
                margin-bottom: 20px;

                font-size: 24px;
                font-weight: 700;
            }
            
        }
        .reviews {
            &__title {
                margin-bottom: 20px;
                font-size: 24px;
                font-weight: 700;
            }
            &__username-wrapper {
                display: flex;
                align-items: center;
                gap: 30px;
                margin-bottom: 20px;
            }
            &__username {
                font-size: 18px;
                font-weight: 700;
            }
            &__text {
                margin-left: 20px;
                font-size: 18px;
            }
        }
    }

    
</style>