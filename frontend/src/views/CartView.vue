<template lang="en">
    <div class="cart-page">
        <div class="cart-page__wrapper">
            <div class="cart-page__title">
                <h1 class="title">Корзина</h1>
            </div>
            <div class="column is-12 box" v-if="cartTotalLength">
                <table class="table is-fullwidth" >
                    <thead>
                        <tr>
                            <th>Товар</th>
                            <th>Цена</th>
                            <th>Количество</th>
                            <th>Общая стоимость</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="item in cart.items" v-bind:key="item.product.id">
                            <td><router-link :to="'/product/' + item.product.id" >{{ item.product.name }}</router-link></td>
                            <td>${{ item.product.price }}</td>
                            <td>
                                {{ item.quantity }}
                            </td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                            <td><button class="delete"></button></td>
                        </tr>
                    </tbody>
                </table>
                <div class="column is-12 box">
                    <h2 class="cart-page__summary-title">Стоимость</h2>

                    <p class="cart-page__price-summary"><strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} товаров</p>

                    <hr>
                    <div class="cart-page__button-wrapper">
                        <router-link to="/cart/checkout" class="cart-page__checkout-link">Перейти к оформлению</router-link>
                    </div>
                </div>
            </div>
            <div class="no-items" v-else>
                Корзина пуста...
            </div>
        </div>
        

    </div>
</template>
<script>
import axios from 'axios';
import CartItem from '@/components/CartItem.vue'

export default {
    name: 'CartView',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        // this.user()
        this.cart = this.$store.state.cart
        console.log(this.cart.items)
    },
    methods: {
        user() {
            axios
            .get(`/api/v1/`,
            {
                withCredentials: true,
            }
            )
            .then(response => {
                this.data = response.data
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
        })
        },
        getItemTotal(item) {
            return item.quantity * item.product.price
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        }
    }
}
</script>
<style lang="scss">
table {
	width: 100%;
	border: none;
	margin-bottom: 20px;
	border-collapse: separate;
}
table thead th {
	font-weight: bold;
	text-align: left;
	border: none;
	padding: 10px 15px;
	background: #EDEDED;
	font-size: 14px;
	border-top: 1px solid #ddd;
}
table tr th:first-child, table tr td:first-child {
	border-left: 1px solid #ddd;
}
table tr th:last-child, table tr td:last-child {
	border-right: 1px solid #ddd;
}
table thead tr th:first-child {
	border-radius: 20px 0 0 0;
}
table thead tr th:last-child {
	border-radius: 0 20px 0 0;
}
table tbody td {
	text-align: left;
	border: none;
	padding: 10px 15px;
	font-size: 14px;
	vertical-align: top;
}
table tbody tr:nth-child(even) {
	background:#EDEDED;

}
table tbody tr:last-child td{
	border-bottom: 1px solid #ddd;
}
table tbody tr:last-child td:first-child {
	border-radius: 0 0 0 20px;
}
table tbody tr:last-child td:last-child {
	border-radius: 0 0 20px 0;
}

.cart-page {
    background-color: white;
    box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.2);
    border-radius: 5px;
    padding: 30px;
    padding-left: 80px;
    margin-top: 30px;
    min-height: 300px;
    &__title {
        font-size: 30px;
        font-weight: 700;
        // text-align: center;
        // margin-top: 20px;
        margin-bottom: 15px;
        margin-top: 20px;
        color: #151528;
        letter-spacing: 0.1px;
    }
}
.cart-page__summary-title {
    text-align: end;
}
.cart-page__price-summary {
    text-align: end;

}
.cart-page__button-wrapper {
    display: flex;
    justify-content: flex-end;
}
.cart-page__checkout-link {
}
</style>