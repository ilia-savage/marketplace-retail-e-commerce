<template lang="en">
    <div class="auth-page-wrapper">
        <h1 class="auth-page-title">Вход</h1>
        {{ status }}
        <p v-show="error">error</p>
        <div class="auth-wrapper">
            <div class="auth-wrapper__form">
                <label class="auth-wrapper__label" for="code">Код</label>
                <input class="auth-wrapper__input" type="text" placeholder="Пример: 123456" id="code" v-model="code" required>
                <div class="button-wrapper">
                    <button class="auth-wrapper__auth-button" @click="login()">
                        <img class="auth-wrapper__auth-image" src="@/assets/img/login-button.svg" alt="auth-button" width="150">
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            code: ''
        }
    },
}
</script>
<style lang="scss">
    .auth-page-wrapper {
    background-color: white;
    margin: 0 auto;
    max-width: 700px;
    height: 400px;
    box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.2);
    border-radius: 5px;
    padding: 30px;
    margin-top: 30px;
}
.auth-wrapper {
    margin: 0 auto;
    width: 300px;

    &__auth-button{
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
.auth-page-title {
    font-size: 28px;
    font-weight: 700;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

.auth-wrapper__input {
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