<template lang="en">
    <div class="login-page-wrapper">
        <h1 class="login-page-title">Вход</h1>
        {{ status }}
        <p v-show="error">error</p>
        <div class="login-wrapper">
            <div class="login-wrapper__form">
                <label class="login-wrapper__label" for="email">E-mail</label>
                <input class="login-wrapper__input" type="email" placeholder="E-mail" id="email" v-model="email" autocomplete="email" required>
                <br>
                <label class="login-wrapper__label" for="password">Пароль</label>
                <input class="login-wrapper__input" type="password" placeholder="Пароль" id="password" v-model="password" autocomplete="current-password" required> 
                <div class="button-wrapper">
                    <button class="login-wrapper__login-button" @click="login()">
                        <img class="login-wrapper__login-image" src="@/assets/img/login-button.svg" alt="login-button" width="150">
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
            status: '',
            name: '',
            last_name: '',
            email: '',
            password: '',
            error: false,
        }
    },
    created() {
        console.log('check')
        this.$emit('check-login')
    },
    methods: {
        async login() {
            console.log(this.email, this.password)
            await axios
                .post('/api/v1/login/', {
                    "username": this.email,
                    "password": this.password
                },
                {
                    withCredentials: true
                }
                    
                )
                .then(response => {
                    console.log(response.data)
                    this.error = false
                    this.status = response.data.message
                    this.$emit('detail')
                    this.$router.push('/')
                    // this.$forceUpdate();
                })
                .catch(error => {
                    console.log(error)
                    this.error = true
                })
        }
    },
}
</script>
<style lang="scss">
.login-page-wrapper {
    background-color: white;
    margin: 0 auto;
    max-width: 700px;
    height: 400px;
    box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.2);
    border-radius: 5px;
    padding: 30px;
    margin-top: 30px;
}
.login-wrapper {
    margin: 0 auto;
    width: 300px;

    &__login-button{
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
.login-page-title {
    font-size: 28px;
    font-weight: 700;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

.login-wrapper__input {
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