
<template>
  <b-container id="categories" class="align-content-center">
    <b-row class='header'>
      <b-col class='col-12'>
      <Header
      :headerText="'Please choose a category'"
      />
      </b-col>
    </b-row>
    <b-row class="catBoxes align-content-center justify-content-center">
      <b-row
      class="catBox col-10 m-2 mb-4 green align-content-center"
      @mouseover="relationshipHover = true"
      @mouseleave="relationshipHover = false"
      :class="{hover: relationshipHover, green: !relationshipHover}"
      >
        <router-link
        :to="{ name: 'Classic', params: { relationshipPath } }"
        >
        <p class="ml-5">Parkort</p>
        <img src='../assets/icons/relationship.svg' class="h-100 w-100"/>
        </router-link>
      </b-row>
      <b-row class="catBox col-10 m-2 mb-4 blue align-content-center">
        <router-link :to="{ name: 'Classic', params: { friendsPath } }">
        <p class="ml-5">Vennekort</p>
        <img src='../assets/icons/relationship.svg' class="h-100 w-100 img-fluid"/>
        </router-link>
      </b-row>
      <b-row class="catBox col-10 m-2 mb-4 purple align-content-center">
        <router-link :to="{ name: 'Classic', params: { challengesPath } }">
        <p class="ml-5">Utfordinger</p>
        <img src='../assets/icons/relationship.svg' class="h-100 w-100 img-fluid"/>
        </router-link>
      </b-row>
      <b-row
      class="catBox deactive col-10 m-2 mb-4 orange align-content-center"
      >
        <!-- <router-link :to="{ name: 'Classic', params: { cardsPath } }" !-->
        <p class="ml-5">Dilemmaer</p>
        <img src='../assets/icons/relationship.svg' class="h-100 w-100 img-fluid"/>
        <!-- </router-link> !-->
      </b-row>
    </b-row>
  </b-container>
</template>

<script>
import Header from './Header.vue'

export default {
  name: 'Categories',
  data () {
    return {
      relationshipPath: 'http://127.0.0.1:5000/parkort',
      friendsPath: 'http://127.0.0.1:5000/vennekort',
      challengesPath: 'http://127.0.0.1:5000/utfordring'
    }
  },
  components: {
    Header
  }
}
</script>

<style lang="scss">
@import "../styles/index.scss";

#categories {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  text-align: center;
  overflow: hidden;
  padding: 0;
  // box-shadow: 10px black;
}

a:hover {
  color: none;
  text-decoration-line: none;
}

img {
  opacity: 10%;
  position: absolute;
  right: 0;
  left: 20vw;
  top: 0;
}

p {
  color: white;
  text-shadow: 0px 1px black;
  font-size: 1.5rem;
  margin-bottom: 0;
  z-index: 1;
  vertical-align: middle;
  position: relative;
}

.catBox {
  height: 15vh;
  border-radius: 30px;
  box-shadow: 0px 5px rgba($color: #000000, $alpha: 0.4);
  overflow: hidden;
  padding: 0;
  transition: scale(2);
}

.catBox:hover {
  color: white;
  text-shadow: none;
  opacity: 90%;
  box-shadow: 0px 10px rgba(0, 0, 0, 0.3);
  border: solid 2px;
  border-color: lightgray;
}

.deactive {
  opacity: 20% !important;
  border: none !important;
}

.green {
  background-size: cover;
  background-image: linear-gradient( #00B894, #259B7A);
}

.blue {
  background-size: cover;
  background-image: linear-gradient( #0984E3, #4F89C4);
}

.purple {
  background-size: cover;
  background-image: linear-gradient( #7B74CE, #6C5CE7);
}

.orange {
  background-size: cover;
  background-image: linear-gradient( #D35031, #D35A3E);
}
</style>
