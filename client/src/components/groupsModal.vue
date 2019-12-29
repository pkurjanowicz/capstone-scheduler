<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                <label>Group Name:</label>
                <input v-model="groupName" v-on:keyup.enter="submitNewGroup"/>
                </slot>
            </section>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import VueTags from "vue-tags"

let moment = require('moment')

export default {
    name: "groupsModal",
    data() {
        return {
            userID: '',
            groupName: '',
            
        }

    },
    components: {
        VueTags
    },
    props: ['userID', 'groupName'],
    methods: {
        submitNewGroup() {
            console.log("user_id line 37   "  + this.userID)
            axios.post('/newgroup', { owner_id: this.userID, group_name: this.groupName })
            .then((response) => {
                this.groupName = ''
                this.currentGroupId = response.data.group_id
                
             })

        },



        close() {
        this.$emit('close');
        },
        
    }
}
</script>

<style scoped>

</style>