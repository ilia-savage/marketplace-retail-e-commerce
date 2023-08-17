<template lang="en">
    <div class="checkout-wrapper">
        <input type="text" placeholder="Имя" v-model="name">
        <input type="text" placeholder="Фамилия" v-model="last_name">
        <input type="number" placeholder="Номер телефона" v-model="number">
        <input type="text" placeholder="Город" v-model="city">
        <input type="text" placeholder="Адрес" v-model="address">
    </div>
</template>
<script>
export default {
    data() {
        return {
            name: '',
            last_name: '',
            number: '',
            city: '',
            address: ''
        }
    },
}
</script>
<style lang="scss">
    
</style>