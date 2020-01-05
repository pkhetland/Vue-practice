
<template>
  <b-container fluid id="classic" class="h-100">
    <b-row class='header'>
      <b-col class='col-12'>
      <Header/>
      </b-col>
    </b-row>
    <b-row
    class="stack justify-content-center mr-0 ml-0"
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
    <b-row class="footer justify-content-center align-content-center">
      <Footer
      @triggerStarCard="starCard"
      @increaseRating="increaseRating"
      @decreaseRating="decreaseRating"
      @nextCard="removeCardFromDeck"
      />
    </b-row>
  </b-container>
</template>

<script>
import GameCardsStack from './GameCardsStack.vue'
import Header from './Header.vue'
import Footer from './Footer.vue'
import axios from 'axios'

export default {
  name: 'Classic',
  components: {
    Header,
    GameCardsStack,
    Footer
  },
  props: {
    relationshipPath: {
      type: String,
      default: null
    },
    friendsPath: {
      type: String,
      default: null
    },
    challengesPath: {
      type: String,
      default: null
    }
  },
  data () {
    return {
      visibleCards: [],
      outOfCards: false
    }
  },
  methods: {
    getCards () {
      if (this.relationshipPath) {
        axios.get(this.relationshipPath)
          .then((res) => {
            this.visibleCards = res.data
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
          })
      } else if (this.friendsPath) {
        axios.get(this.friendsPath)
          .then((res) => {
            this.visibleCards = res.data
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
          })
      } else if (this.challengesPath) {
        axios.get(this.challengesPath)
          .then((res) => {
            this.visibleCards = res.data
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
          })
      }
    },
    updateCard (payload) {
      axios.post(this.cardsPath, payload)
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        })
    },
    increaseRating () {
      const payload = {
        function: 'increase',
        id: this.visibleCards[0]['id'],
        rating: this.visibleCards[0]['rating']
      }
      this.updateCard(payload)
    },
    decreaseRating () {
      const payload = {
        function: 'decrease',
        id: this.visibleCards[0]['id'],
        rating: this.visibleCards[0]['rating']
      }
      this.updateCard(payload)
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
    starCard () {
      alert('Card has been starred!')
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

.header {
  height: 15vh;
}

.stack {
  height: 70vh;
}

.footer {
  height: 15vh;
}

.gamecardstack {
  margin-bottom: 20px;
  margin-left: 20px;
  margin-right: 20px;
  position: relative;
}

.outOfCards {
  color: white;
}

</style>
