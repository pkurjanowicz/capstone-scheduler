<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                    <div>
                        {{ title }}<br><br>
                        {{ details }}
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
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
}

.modal {
    background: #FFFFFF;
    display: flex;
    flex-direction: column;
    border: 3px solid blue;
    padding: 3%;
    height: 200px;
    width: 80%;
}

.modal-header {
    padding: 20px 20px 0 20px;
    display: flex;
}

.x-out-button {
    margin-left: auto;
    order: 2;
}
</style>