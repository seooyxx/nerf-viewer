const baseUrl = "http://34.81.142.201:8080/data/model_1/scene/";
const avatarBaseUrl = "http://34.81.142.201:8080/data/model_1/avatar/";

async function loadSceneAndAvatar(sceneName, avatarName) {
    const sceneResponse = await fetch(`${baseUrl}${sceneName}/scene_1_mlp.json`);
    const sceneData = await sceneResponse.json();

    const avatarResponse = await fetch(`${avatarBaseUrl}${avatarName}/${avatarName}.json`);
    const avatarData = await avatarResponse.json();

    // 데이터를 사용하여 scene과 avatar를 처리
    console.log(sceneData, avatarData);
}

// 함수 호출 예시
loadSceneAndAvatar("scene_1", "avatar_1");
