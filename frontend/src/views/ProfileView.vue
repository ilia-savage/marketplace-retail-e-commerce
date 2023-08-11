<template lang="en">
    <div>
        {{ order }}
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            order: {}
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
                    this.order = response.data.results
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
}
</script>
<style lang="scss">
    
</style>