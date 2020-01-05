
<template>
  <b-container fluid id="game">
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
      @hideCard="removeCardFromDeck"
      @triggerChangePlayer="changePlayer"/>
      <b-row v-else-if='outOfCards' class='outOfCards'>
        <b-col>You have run out of cards!</b-col>
      </b-row>
    </b-row>
    <b-row>
      <b-col>
        <Footer
        @triggerStarCard="starCard"
        @triggerChangePlayer="changePlayer"
        @nextCard="removeCardFromDeck"
        />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import GameCardsStack from './GameCardsStack.vue'
import Header from './Header.vue'
import Statusbar from './Statusbar.vue'
import Footer from './Footer.vue'
import axios from 'axios'

export default {
  name: 'GameMode',
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
          avatar: 'https://pickaface.net/gallery/avatar/51139124_200101_2051_aseu.png',
          active: false
        },
      visibleCards: [],
      outOfCards: false
    }
  },
  methods: {
    getCards () {
      const path = 'http://localhost:5000/cards'
      axios.get(path)
        .then((res) => {
          this.visibleCards = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
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
    },
    changePlayer () {
      this.player1.active = !this.player1.active
      this.player2.active = !this.player2.active
    },
    starCard () {
      alert('Card has been starred!')
    },
    startOver () {
      this.visibleCards = this.visibleCards
    }
  },
  watch: {
    visibleCards () {
      if (this.visibleCards.length === 0) {
        this.outOfCards = true
      }
    }
  },
  created () {
    this.getCards()
  }
}
</script>

<style lang="scss">

#game {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  text-align: center;
  height: 720px;
  width: 375px;
  background-size: cover;
  background-color: #190048;
  overflow: hidden;
  padding: 0;
  border: solid 7px;
  border-color: black;
  border-radius: 20px;
  // box-shadow: 10px black;
}

.gamecardstack {
  margin-top: 40px;
  margin-left: 20px;
  margin-right: 20px;
  position: relative;
  height: 100vw;
  max-height: 450px;
}

.outOfCards {
  color: white;
}

</style>
