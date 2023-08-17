<template lang="en">
    <div class="profile-wrapper">
        <h1 class="profile-title">
            Ваши заказы
        </h1>

        <div class="order-card" v-for="order in orders" v-bind:key="order.id">
            <div class="order-card__wrapper">
                <div class="order-card__products">
                    <p class="order-card__title">
                        <strong>Заказ №{{ order.id }}</strong>
                    </p>
                    <div class="order-card__product-card" v-for="product in order.products" v-bind:key="product.id">
                        <div class="order-card__product-wrapper">
                            <div class="order-card__product-image">
                                <img :src="product.thumbnail" alt="thumbnail" width='100'>
                            </div>
                            <div class="order-card__product-info">
                                <router-link :to="'/product/' + product.id" class="order-card__name">{{ product.category.name }} {{ product.name }} </router-link><span class="order-card__quantity">Количество: {{ product.quantity }}</span>
                                <p class="order-card__price">Цена: {{ product.price }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="order-card__info">
                    <p class="order-card__title">
                        <strong>Информация</strong>
                    </p>
                    <p class="order-card__text">
                        <strong>Имя получателя:</strong> <span>{{ order.name }}</span>
                    </p>
                    <p class="order-card__text">
                        <strong>Фамилия получателя:</strong> <span>{{ order.last_name }}</span>
                    </p>
                    <p class="order-card__text">
                        <strong>Номер телефона:</strong> <span>{{ order.phone_number }}</span>
                    </p>
                    <p class="order-card__text">
                        <strong>Город:</strong> <span>{{ order.city }}</span>
                    </p>
                    <p class="order-card__text">
                        <strong>Адрес:</strong> <span>{{ order.address }}</span>
                    </p>
                </div>
            </div>
            <hr>

        </div>

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
    created() {
        this.getOrders()
        this.$emit('check-login-profile')

    },
    methods: {
        async getOrders() {
            await axios
                .get("/api/v1/order/",
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


.order-card__name {
    text-decoration: none;
    color: blue;

    &:hover {
        text-decoration: underline;
    }
}

.order-card__wrapper {
    display: flex;
    column-gap: 100px;
    margin: 20px 0;
    flex-wrap: wrap;
}

.order-card__title {
    margin-bottom: 20px;
    font-size: 20px;
}
.order-card__product-card {
    margin-bottom: 20px;

    &:last-child {
        margin-bottom: 0;
    }
}
.order-card__price {
    margin-top: 5px;
}
.order-card__product-image {
    display: flex;
    flex-direction: column;
    // align-items: center;
    justify-content: center;
}
.order-card__text {
    margin-top: 5px;
}
.order-card__product-wrapper {
    display: flex;
    gap: 10px;
}
.order-card__product-info {
    display: flex;
    flex-direction: column;
    // align-items: center;
    justify-content: center;
}
</style>