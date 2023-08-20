<template lang="en">
    <div class="checkout-page-wrapper">
        <h1 class="checkout-page-title">Оформление</h1>
        <p v-show="error">error</p>
        <div class="checkout-wrapper">
            <div class="checkout-wrapper__form">
                <label class="checkout-wrapper__label" for="name">Имя</label>
                <input class="checkout-wrapper__input" type="text" placeholder="Введите ваше имя" id="name" v-model="name" required>
                <br>
                <label class="checkout-wrapper__label" for="last_name">Фамилия</label>
                <input class="checkout-wrapper__input" type="text" placeholder="Введите вашу фамилию" id="last_name" v-model="last_name" required>
                <br>
                <label class="checkout-wrapper__label" for="phone">Номер телефона</label>
                <input class="checkout-wrapper__input" type="text" placeholder="Введите ваш номер телефона" id="phone" v-model="number" required>
                <br>
                <label class="checkout-wrapper__label" for="city">Город</label>
                <input class="checkout-wrapper__input" type="text" placeholder="Город" id="city" v-model="city" required>
                <br>
                <label class="checkout-wrapper__label" for="address">Адрес</label>
                <input class="checkout-wrapper__input" type="text" placeholder="Ваш адрес" id="address" v-model="address" required>
                <br>
                
                <div class="button-wrapper">
                    <button class="checkout-wrapper__checkout-button" @click="sendOrder()">
                        <img class="checkout-wrapper__checkout-image" src="@/assets/img/login-button.svg" alt="checkout-button" width="150">
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            name: '',
            last_name: '',
            number: '',
            city: '',
            address: '',
            cart: {
                items: []
            },
            products: []
        }
    },
    created() {
        // this.user()
        this.cart = this.$store.state.cart
        console.log(this.cart.items)
        // creating products array
        this.cart.items.forEach(element => {
            console.log(element.product.id)
            console.log(element.quantity)
            this.products.push({
                "product": element.product.id,
                "quantity": element.quantity
            })
        });
        console.log(this.products, 'products')
        
    },
    methods: {
        async sendOrder() {
            axios
                .post('/api/v1/order/create/', {
                    "products": this.products,
                    "name": this.name,
                    "last_name": this.last_name,
                    "phone_number": this.number,
                    "city": this.city,
                    "address": this.address
                },
                {
                    withCredentials: true
                })
                .then(response => {
                    console.log(response)
                    this.$store.commit('clearCart')
                    this.$emit("cart-rerender")
                    this.$router.push('/success')
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
<style lang="scss">
    .checkout-page-wrapper {
    background-color: white;
    margin: 0 auto;
    max-width: 700px;
    box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.2);
    border-radius: 5px;
    padding: 30px;
    margin-top: 30px;
}
.checkout-wrapper {
    margin: 0 auto;
    width: 300px;

    &__checkout-button{
        // right: 45px;
        // top: 15px;
        // display: inline;
        background-color: white;
        width: 150px;
        // border-radius: 50%;
        outline: none;
        border: transparent;
        cursor: pointer;
    }
}
.button-wrapper {
    display: flex;
    justify-content: center;
}
.checkout-page-title {
    font-size: 28px;
    font-weight: 700;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

.checkout-wrapper__input {
    background-color: #efeff2;
    font-size: 16px;
    border: white;
    outline: none;
    width: 100%;
    height: 58px;
    position: relative;
    border-radius: 10px;
    padding-left: 20px;
    transition: all 0.3s;
    border: 1px solid #d7d4d4;
    margin-bottom: 15px;
    margin-top: 10px;


    &:hover{
        background-color: white;
        border: 1px solid #d7d4d4;

        // border: 2px solid rgb(189, 189, 189);
        box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 15px;
    }
    &:focus{
        background-color: white;
        border: 1px solid #d7d4d4;

        // border: 2px solid rgb(189, 189, 189);
        box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 15px;
    }
}
</style>