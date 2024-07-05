import React from "react";

const styles = {
    wrapper: {
        padding: 16,
        display: "flex",
        flexDirection: "row",
        borderBottom: "1px solid grey",
    },
    greeting: {
        marginRight: 8,
    },
};

function Toolbar(props) {
    // 3개의 props를 받음
    const { isLoggedIn, onClickLogin, onClickLogout } = props;

    return (
        <div style={styles.wrapper}>
            {/* isLoggedIn 뒤는 항상 참(문자열) */}
            {/* isLoggedIn이 true이면 && 뒤가 렌더링됨 */}
            {/* isLoggedIn이 false이면 && 뒤의 코드는 계산에서 아예 제외됨 (확정적인 제외) */}
            {isLoggedIn && <span style={styles.greeting}>환영합니다!</span>}

            {isLoggedIn ? (
                <button onClick={onClickLogout}>로그아웃</button>
            ) : (
                <button onClick={onClickLogin}>로그인</button>
            )}
        </div>
    );
}

export default Toolbar;