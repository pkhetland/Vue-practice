
<template>
  <b-container fluid
  id="app"
  >
    <!-- GameCardStack row -->
    <b-row class='header'>
      <b-col class='col-12'>
      <Header/>
      </b-col>
    </b-row>
    <b-row class='statusbar'>
      <Statusbar v-bind:player1="player1" v-bind:player2="player2"/>
    </b-row>
    <b-row
    class="row gamecardstack align-content-center justify-content-center"
    >
      <GameCardsStack
      v-if='!outOfCards'
      :cards="visibleCards"
      @cardAccepted="handleCardAccepted"
      @cardRejected="handleCardRejected"
      @cardSkipped="handleCardSkipped"
      @hideCard="removeCardFromDeck"/>
      <h2 v-else-if='outOfCards' class='outOfCards'>
        You have run out of cards!
      </h2>
      <router-view/>
    </b-row>
    <b-row>
      <b-col>
        <Footer/>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import GameCardsStack from './components/GameCardsStack.vue'
import Header from './components/Header.vue'
import Statusbar from './components/Statusbar.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Statusbar,
    GameCardsStack,
    Footer
  },

  data () {
    return {
      player1:
        {
          name: 'Tomas',
          avatar: 'https://pickaface.net/gallery/avatar/unr_sample_161118_2054_ynlrg.png',
          active: true
        },
      player2:
        {
          name: 'Mirjam',
          avatar: 'https://pickaface.net/gallery/avatar/unr_yassine_191124_2012_3gngr.png',
          active: false
        },
      visibleCards: [
        {
          id: 1,
          title: 'Test 1',
          text: 'This is the first card'
        },
        {
          id: 2,
          title: 'Test 2',
          text: 'This is the second card'
        },
        {
          id: 3,
          title: 'Test 3',
          text: 'This is the third card'
        }
      ],
      outOfCards: false
    }
  },
  methods: {
    handleCardAccepted () {
      // eslint-disable-next-line
      console.log('handleCardAccepted');
    },
    handleCardRejected () {
      // eslint-disable-next-line
      console.log('handleCardRejected');
    },
    handleCardSkipped () {
      // eslint-disable-next-line
      console.log('handleCardSkipped');
    },
    removeCardFromDeck () {
      this.visibleCards.shift()
    }
  },
  watch: {
    visibleCards () {
      if (this.visibleCards.length === 0) {
        this.outOfCards = true
      }
    }
  }
}
</script>

<style lang="scss">

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  text-align: center;
  height: 720px;
  width: 375px;
  background-size: cover;
  background-color: #190048;
  overflow: hidden;
  padding: 0;
}

.gamecardstack {
  margin-top: 40px;
  margin-left: 20px;
  margin-right: 20px;
  position: relative;
  height: 100vw;
  max-height: 450px;
}

</style>
