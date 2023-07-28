<template lang="">
    <div>
        
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'CartView',
    data() {
        return {
            
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