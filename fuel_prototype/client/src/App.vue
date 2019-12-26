
<template>
  <div
  class='container-fluid '
  id="app"
  >
    <div class='row'>
      <div class='col-12' id='window'>
        <!-- GameCardStack row -->
        <div class='row header'>
          <div class='col-12'>
          <Header/>
          </div>
        </div>
        <div
        class="row align-content-center justify-content-center"
        >
          <div
          class="col-10 mt-5 mb-5"
          id='main'
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
          </div>
                <div class="col-md-5 col-sm-10 col-lg-10">
            <Timer/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GameCardsStack from './components/GameCardsStack.vue';
import Header from './components/Header.vue';
import Timer from './components/Timer.vue';

export default {
  name: 'App',
  components: {
    GameCardsStack,
    Header,
    Timer,
  },

  data() {
    return {
      visibleCards: [
        {
          id: 1,
          title: 'Test 1',
          text: 'This is the first card',
        },
        {
          id: 2,
          title: 'Test 2',
          text: 'This is the second card',
        },
        {
          id: 3,
          title: 'Test 3',
          text: 'This is the third card',
        },
      ],
      outOfCards: false,
    };
  },
  methods: {
    handleCardAccepted() {
      // eslint-disable-next-line
      console.log('handleCardAccepted');
    },
    handleCardRejected() {
      // eslint-disable-next-line
      console.log('handleCardRejected');
    },
    handleCardSkipped() {
      // eslint-disable-next-line
      console.log('handleCardSkipped');
    },
    removeCardFromDeck() {
      this.visibleCards.shift();
    },
  },
  watch: {
    visibleCards() {
      if (this.visibleCards.length === 0) {
        this.outOfCards = true;
      }
    },
  },
};
</script>

<style lang="scss">
@import "./styles/mixins.scss";

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  text-align: center;
  height: 720px;
  width: 375px;
  background-size: cover;
  background-color: #190048;
  overflow: hidden;
}

#main {
  height: 100%;
}

</style>
