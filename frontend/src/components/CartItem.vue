<template lang="en">
    <div>
        <tr>
        <td><router-link  >{{ item.product.name }}</router-link></td>
        <td>${{ item.product.price }}</td>
        <td>
            {{ item.quantity }}
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete"></button></td>
        </tr>
    </div>
</template>
<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        }
    },
}
</script>
<style lang="">
    
</style>