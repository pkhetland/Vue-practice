<template>
  <b-container fluid id="app">
    <router-view/>
  </b-container>
</template>

<style lang="scss" scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  text-align: center;
  background-size: cover;
  background-image: linear-gradient(#190048, #0e0027);
  overflow: hidden;
  padding: 0;
  height: 100vh;
  width: 100vw;
  // box-shadow: 10px black;
}
</style>
