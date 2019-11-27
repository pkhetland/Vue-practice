<template>
  <div
    id="app"
    class="min-h-screen w-screen bg-gray-200 flex flex-col pt-20 justify-center items-center md:items-start md:flex-row"
  >
    <div class="w-full max-w-md text-center px-3">
      <h1 class="mb-2 text-gray-700 font-semibold font-sans tracking-wide">Kompani 1</h1>
      <draggable
        tag="ul"
        group="all-users"
        class="draggable-list"
        ghost-class="moving-card"
        filter=".action-button"
        :list="users"
        :animation="200"
      >
        <user-card
          v-for="user in users"
          :user="user"
          :key="user.id"
          @on-edit="onEdit"
          @on-delete="onDelete"
        ></user-card>
      </draggable>
    </div>

    <div class="w-full max-w-md md:ml-6 text-center px-3">
      <h1 class="mb-2 text-gray-700 font-semibold font-sans tracking-wide">Kompani 2</h1>
      <draggable
        tag="ul"
        group="all-users"
        class="draggable-list"
        ghost-class="moving-card"
        filter=".action-button"
        :list="newUsers"
        :animation="200"
      >
        <user-card
          v-for="user in newUsers"
          :user="user"
          :key="user.id"
          @on-edit="onEdit"
          @on-delete="onDelete"
        ></user-card>
      </draggable>
    </div>
  </div>
</template>


<script>
import Draggable from "vuedraggable";
import UserCard from "./components/UserCard";
import './assets/css/tailwind.css'

export default {
  name: "App",
  components: {
    Draggable,
    UserCard
  },
  data() {
    return {
      users: [
        {
          id: 1,
          name: "Max Manus",
          avatar:
            "https://pickaface.net/gallery/avatar/unr_sample_161118_2054_ynlrg.png"
        },
        {
          id: 2,
          name: "Ingebjørg Skoghaug",
          avatar: "https://pickaface.net/gallery/avatar/freud51c8b3f65e7dc.png"
        },
        {
          id: 3,
          name: "Einar Skinnarland",
          avatar: "https://pickaface.net/gallery/avatar/Opi51c74d0125fd4.png"
        },
        {
          id: 4,
          name: "'Tante'",
          avatar:
            "https://pickaface.net/gallery/avatar/unr_yassine_191124_2012_3gngr.png"
        },
        {
          id: 5,
          name: "Gunnar Sønsteby",
          avatar:
            "https://pickaface.net/gallery/avatar/elmedinilla541c03412955c.png"
        }
      ],
      newUsers: [
        {
          id: 6,
          name: "Joachim Rønneberg",
          avatar: "https://pickaface.net/gallery/avatar/Opi51c74d0125fd4.png"
        },
        {
          id: 7,
          name: "Gregers Gram",
          avatar:
            "https://pickaface.net/gallery/avatar/unr_yassine_191124_2012_3gngr.png"
        },
        {
          id: 8,
          name: "Martin Linge",
          avatar:
            "https://pickaface.net/gallery/avatar/elmedinilla541c03412955c.png"
        },
        {
          id: 9,
          name: "Claus Helberg",
          avatar:
            "https://pickaface.net/gallery/avatar/unr_sample_161118_2054_ynlrg.png"
        },
        {
          id: 10,
          name: "Sverre Granlund",
          avatar: "https://pickaface.net/gallery/avatar/freud51c8b3f65e7dc.png"
        }
      ]
    };
  },
  methods: {
    onEdit(user) {
      alert(`Editing ${user.name}`);
    },
    onDelete(user) {
      alert(`Deleting ${user.name}`);
    }
  }
};
</script>

<style>
.draggable-list {
  min-height: 100px;
}
/* Unfortunately @apply cannot be setup in codesandbox,
but you'd use "@apply border opacity-50 border-blue-500 bg-gray-200" here */
.moving-card {
  opacity: 0.5;
  background: #F7FAFC;
  border: 1px solid #4299e1;
}
</style>
