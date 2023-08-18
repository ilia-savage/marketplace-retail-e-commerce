<template lang="en">
    <div class="checkout-wrapper">
        <input type="text" placeholder="Имя" v-model="name">
        <input type="text" placeholder="Фамилия" v-model="last_name">
        <input type="text" placeholder="Номер телефона" v-model="number">
        <input type="text" placeholder="Город" v-model="city">
        <input type="text" placeholder="Адрес" v-model="address">
    </div>
    <button @click="sendOrder()">К оплате</button>
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
    
</style>