<template lang="en">
    <div class="profile-wrapper">
        <div class="profile-avatar-wrapper">
            <img class="profile-avatar" src="@/assets/img/avatar.webp" alt="avatar" width="150">
        </div>
        <p class="profile-username">{{ user.name }}</p>
        <div class="profile-button-wrapper">
            <button @click="logout()" class="profile-logout-button">Выйти из аккаунта</button>
        </div>
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
            orders: {},
            user: ''
        }
    },
    created() {
        this.getOrders()
        this.detail()
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
        },
        async detail() {
            await axios
            .get(`/api/v1/`,
            {
                withCredentials: true,
            }
            )
            .then(response => {
                this.user = response.data
                this.anonymous = false
                this.forceRerender()
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            })
        },
        async logout() {
            await axios
            .get(`/api/v1/logout/`,
            {
                withCredentials: true,
            }
            )
            .then(response => {
                this.$router.go()
                console.log(response)
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
.profile-logout-button{
    display:inline-block;
    padding:0.3em 1.2em;
    margin:0 0.1em 0.1em 0;
    border:0.16em solid rgba(255,255,255,0);
    border-radius:2em;
    box-sizing: border-box;
    text-decoration:none;
    font-family:'Roboto',sans-serif;
    font-weight:300;
    color:#FFFFFF;
    text-shadow: 0 0.04em 0.04em rgba(0,0,0,0.35);
    text-align:center;
    transition: all 0.2s;
    background-color:#f14e4e;
    cursor: pointer;
    @media all and (max-width:30em){  
        display:block;
        margin:0.2em auto;
    }
}
.profile-logout-button:hover{
    border-color: rgba(255,255,255,1);
}

.profile-username {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 15px;
    text-align: center;
}
.profile-avatar-wrapper{
    display: flex;
    justify-content: center;
}
.profile-button-wrapper {
    display: flex;
    justify-content: center;
    margin-bottom: 50px;
}
.order-card__products {
    width: 480px;
}
</style>