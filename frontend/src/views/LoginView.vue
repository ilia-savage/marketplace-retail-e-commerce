<template lang="">
    <div>
        
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            
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