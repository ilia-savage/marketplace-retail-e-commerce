<template lang="">
    <div>
        {{status}}
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            status: '',
        }
    },
    mounted() {
        this.login()
    },
    methods: {
        login() {
            axios
            .post('/api/v1/login/', {
                    "username": "admin@admin.admin",
                    "password": "admin"
            },
            {
                withCredentials: true,
            }
            )
            .then(response => {
                console.log(response.data)
                this.status = response.data.message
            })
            .catch(error => {
                console.log(error)
        })
        }
    },
}
</script>
<style lang="">
    
</style>