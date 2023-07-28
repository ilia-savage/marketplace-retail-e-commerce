<template lang="">
    <div>
        {{ data }}
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'CartView',
    data() {
        return {
            data: '',
        }
    },
    mounted() {
        this.user()
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
        }
    }
}
</script>
<style lang="">
    
</style>