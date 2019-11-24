<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                    <div>
                        <p>Here is the title:<br> {{ title }}</p><br><br>
                        <p>Here are the details:<br> {{ details }}</p>
                    </div>
                </slot>
            </section>
        </div>
    </div>
</template>

<script>
export default {
    name: "eventDetailsModal",
    props: ['title', 'details'],
    methods: {
        close() {
        this.$emit('close');
      },
    }
}
</script>

<style scoped>
.modal-backdrop {
    position: static;
    margin: 100% 0 0 0;
}

.modal {
    background: #FFFFFF;
    display: flex;
    flex-direction: column;
    border: 3px solid blue;
    padding: 10%;
    height: 100%;
}

.modal-header {
    display: flex;
}

.x-out-button {
    margin-left: auto;
    order: 2;
}
</style>