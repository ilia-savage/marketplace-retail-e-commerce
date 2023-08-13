<template lang="en">
    <div class="profile-wrapper">
        <h1 class="profile-title">
            Заказы
        </h1>

        <div class="order-card" v-for="order in orders" v-bind:key="order.id">
            <p class="order-card__title">
                Заказ #{{ order.id }}
            </p>
            <div class="order-card__product-card" v-for="product in order.products" v-bind:key="product.id">
                <p class="order-card__title">{{ product.name }} <span>Количество: {{ product.quantity }}</span></p>
                <p class="order-card__price">Цена: {{ product.price }}</p>
            </div>
        </div>

        {{ order }}
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            orders: {}
        }
    },
    mounted() {
        this.getOrders()
    },
    methods: {
        async getOrders() {
            await axios
                .get("http://127.0.0.1:8000/api/v1/order/",
                {
                    withCredentials: true
                })
                .then(response => {
                    console.log(response)
                    this.orders = response.data.results
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
}
</script>
<style lang="scss">
.profile-wrapper {
    background-color: white;
    box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.2);
    border-radius: 5px;
    padding: 30px;
    padding-left: 80px;
    margin-top: 30px;
}
.profile-title {
    font-size: 30px;
    font-weight: 700;
    // text-align: center;
    // margin-top: 20px;
    margin-bottom: 10px;
    color: #151528;
    letter-spacing: 0.1px;
}
.profile-card {
}
</style>