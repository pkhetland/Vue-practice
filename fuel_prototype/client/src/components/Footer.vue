<template>
  <b-container>
    <b-row class='footer justify-content-center align-content-center'>
      <b-col class='icon icon1 col-4'>
        <skip-back-icon size="2x" class="custom-class"/>
      </b-col>
      <b-col class='icon icon2 col-4'>
        <star-icon size="2x" class="custom-class"/>
      </b-col>
      <b-col class='icon icon2 col-4'>
        <skip-forward-icon size="2x" class="custom-class"/>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { SkipBackIcon, StarIcon, SkipForwardIcon } from 'vue-feather-icons'
export default {
  components: {
    SkipBackIcon,
    StarIcon,
    SkipForwardIcon
  }
}
</script>

<style lang="scss" scoped>
.footer {
  margin-bottom: 20px;
  margin-top: 10px;
  color: whitesmoke;
}

.icon {
  display: inline-block
}

</style>
