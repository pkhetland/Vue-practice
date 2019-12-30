<template>
  <b-container class='container-fluid'>
    <b-row class='row statusbar justify-content-center align-content-center'>
      <b-col class='col-4 player notActive'>
        <img class="avatar w-10 h-10 rounded-full" :src="player1.avatar">
        <p class='playerName'>{{ player1.name }}</p>
      </b-col>
      <b-col class='countdownTimer col-4 text-white'>
        <circular-count-down-timer
        :initial-value="30"
        :stroke-width="7"
        :seconds-stroke-color="'#BF0513'"
        :underneath-stroke-color="'#F05D2D'"
        :seconds-fill-color="False"
        :second-label="''"
        :size="100"
        :padding="4"
        :show-second="true"
        :show-minute="false"
        :show-hour="false"
        :show-negatives="false"
        />
      </b-col>
      <b-col class='col-4 player'>
        <img class="avatar w-10 h-10 rounded-full" :src="player2.avatar">
        <p class='playerName'>{{ player2.name }}</p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'Statusbar',
  props: {
    player1: {
      type: Object,
      default: () => ({})
    },
    player2: {
      type: Object,
      default: () => ({})
    }
  },
  data: function () {
    return {
      timer: setInterval(() => this.countdown(), 1000),
      totalTime: 30
    }
  },
  methods: {
    padTime: function (time) {
      return (time < 10 ? '0' : '') + time
    },
    countdown: function () {
      if (this.totalTime >= 1) {
        this.totalTime--
      } else {
        this.totalTime = 0
      }
    }
  },
  computed: {
    minutes: function () {
      const minutes = Math.floor(this.totalTime / 60)
      return this.padTime(minutes)
    },
    seconds: function () {
      const seconds = this.totalTime - (this.minutes * 60)
      return this.padTime(seconds)
    }
  }
}
</script>

<style scoped>
.statusbar {
  height: 80px;
}

.notActive {
  opacity: 50%;
}

.playerName {
  color: whitesmoke;
  margin-top: 10px;
  text-align: center;
}

.avatar {
  display: inline-block;
}

.countdownTimer {
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
}
</style>
