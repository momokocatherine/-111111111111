import streamlit as st
import random
import pandas as pd

# --- 網頁基本設定 ---
st.set_page_config(page_title="通勤單字刷題與複習 App", layout="centered")

# --- 1. 單字資料庫 ---
if "vocab_data" not in st.session_state:
    st.session_state.vocab_data = {
        "第14課": [
            {"word": "つけます II", "meaning": "開（空調等）", "jisho": "つける"},
            {"word": "けします I (消します)", "meaning": "關（空調等）", "jisho": "けす (消す)"},
            {"word": "あけます II (開けます)", "meaning": "開（門、窗等）", "jisho": "あける (開ける)"},
            {"word": "しめます II (閉めます)", "meaning": "關（門、窗等）", "jisho": "しめる (閉める)"},
            {"word": "いそぎます I (急ぎます)", "meaning": "趕快、趕緊", "jisho": "いそぐ (急ぐ)"},
            {"word": "まちます I (待ちます)", "meaning": "等", "jisho": "まつ (待つ)"},
            {"word": "もちます I (持ちます)", "meaning": "拿", "jisho": "もつ (持つ)"},
            {"word": "とります I (取ります)", "meaning": "取", "jisho": "とる (取る)"},
            {"word": "てつだいます I (手伝います)", "meaning": "幫忙", "jisho": "てつだう (手伝う)"},
            {"word": "よびます I (呼びます)", "meaning": "叫", "jisho": "よぶ (呼ぶ)"},
            {"word": "はなします I (話します)", "meaning": "說", "jisho": "はなす (話す)"},
            {"word": "つかいます I (使います)", "meaning": "使用", "jisho": "つかう (使う)"},
            {"word": "とめます II (止めます)", "meaning": "停止", "jisho": "投める (止める)"},
            {"word": "みせます II (見せます)", "meaning": "出示、給～人看", "jisho": "みせる (見せる)"},
            {"word": "おしえます II (教えます)", "meaning": "告訴〔地址〕、教", "jisho": "おしえる (教える)"},
            {"word": "すわります I (座ります)", "meaning": "坐", "jisho": "すわる (座る)"},
            {"word": "たちます I (立ちます)", "meaning": "站立", "jisho": "たつ (立つ)"},
            {"word": "はいります I (入ります)", "meaning": "進入", "jisho": "はいる (入る)"},
            {"word": "でます II (出ます)", "meaning": "離開", "jisho": "でる (出る)"},
            {"word": "ふります I (降ります)", "meaning": "下〔雨〕", "jisho": "ふる (降る)"},
            {"word": "コピーします III", "meaning": "影印", "jisho": "コピーする"},
            {"word": "でんき (電気)", "meaning": "電燈、電氣"},
            {"word": "エアコン", "meaning": "空調"},
            {"word": "パスポート", "meaning": "護照"},
            {"word": "なまえ (名前)", "meaning": "姓名"},
            {"word": "じゅうしょ (住所)", "meaning": "地址"},
            {"word": "ちず (地図)", "meaning": "地圖"},
            {"word": "しお (塩)", "meaning": "鹽"},
            {"word": "さとう (砂糖)", "meaning": "砂糖"},
            {"word": "もんだい (問題)", "meaning": "問題"},
            {"word": "こたえ (答え)", "meaning": "回答、解答"},
            {"word": "よみかた (読み方)", "meaning": "讀法、唸法"},
            {"word": "～かた (～方)", "meaning": "～的方法、～的方式"},
            {"word": "まっすぐ", "meaning": "直直地"},
            {"word": "ゆっくり", "meaning": "慢慢地、好好地"},
            {"word": "すぐ", "meaning": "馬上"},
            {"word": "また", "meaning": "再"},
            {"word": "あとで", "meaning": "等一下、稍候"},
            {"word": "もう すこし (もう 少し)", "meaning": "再～一點"},
            {"word": "もう ～", "meaning": "再～"},
            {"word": "しんごうを みぎへ まがって ください。 (信号を 右へ 曲がって ください。) 【會話】", "meaning": "請在紅綠燈處右轉。"},
            {"word": "これで おねがいします。 (これで お願いします。) 【會話】", "meaning": "我用這個付錢。"},
            {"word": "おつり (お釣り) 【會話】", "meaning": "零錢"},
            {"word": "さあ 【練習C】", "meaning": "那麼（用於提議、催促做某事時）"},
            {"word": "あれ？ 【練習C】", "meaning": "咦？（用於感到驚訝、不可思議時）"},
            {"word": "みどりちょう (みどり町) 【關聯單語】", "meaning": "綠町（虛構的町名）"}
        ],
        "第15課": [
            {"word": "おきます I (置きます)", "meaning": "放置", "jisho": "おく (置く)"},
            {"word": "つくります I (作ります、造ります)", "meaning": "做、製造", "jisho": "つくる (作る、造る)"},
            {"word": "うります I (売ります)", "meaning": "賣", "jisho": "うる (売る)"},
            {"word": "しります I (知ります)", "meaning": "知道", "jisho": "しる (知る)"},
            {"word": "すみます I (住みます)", "meaning": "居住", "jisho": "すむ (住む)"},
            {"word": "けんきゅうします III (研究します)", "meaning": "研究", "jisho": "けんきゅうする (研究する)"},
            {"word": "しりょう (資料)", "meaning": "資料"},
            {"word": "カタログ", "meaning": "目錄、型錄"},
            {"word": "じこくひょう (時刻表)", "meaning": "時刻表"},
            {"word": "ふく (服)", "meaning": "衣服"},
            {"word": "せいひん (製品)", "meaning": "產品"},
            {"word": "ソフト", "meaning": "軟體"},
            {"word": "てんしじしょ (電子辞書)", "meaning": "電子辭典"},
            {"word": "けいざい (経済)", "meaning": "經濟"},
            {"word": "しやくしょ (市役所)", "meaning": "市政府、市公所"},
            {"word": "こうこう (高校)", "meaning": "高中"},
            {"word": "はいしゃ (歯醫者)", "meaning": "牙醫"},
            {"word": "どくしん (獨身)", "meaning": "單身、未婚"},
            {"word": "すみません", "meaning": "對不起、抱歉"},
            {"word": "おもいだします I (思い出します) 【會話】", "meaning": "想起", "jisho": "おもいだす (思い出す)"},
            {"word": "いらっしゃいます I 【會話】", "meaning": "有、在", "jisho": "いらっしゃる"},
            {"word": "みなさん (皆さん) 【練習C】", "meaning": "各位"},
            {"word": "にっぽんばし (日本橋) 【關聯單語】", "meaning": "日本橋（大阪的商業區）"},
            {"word": "みんなのインタビュー 【關聯單語】", "meaning": "大家的採訪（虛構的電視節目名）"}
        ],
        "第16課": [
            {"word": "のります I ［でんしゃに〜］ (乗ります)", "meaning": "坐、搭乘〔電車〕", "jisho": "のる (乗る)"},
            {"word": "おります II ［でんしゃを〜］ (降ります)", "meaning": "下〔電車〕", "jisho": "おりる (降りる)"},
            {"word": "のりかえます II (乗り換えます)", "meaning": "轉乘、換車", "jisho": "のりかえる (乗り換える)"},
            {"word": "あびます II ［シャワーを〜］ (浴びます)", "meaning": "淋〔浴〕", "jisho": "あびる (浴びる)"},
            {"word": "いれます II (入れます)", "meaning": "放入、插入", "jisho": "いれる (入れる)"},
            {"word": "だします I (出します)", "meaning": "拿出、取出、提交", "jisho": "だす (出す)"},
            {"word": "おろします I ［おかねを〜］ (下ろします)", "meaning": "領〔錢〕", "jisho": "おろす (下ろす)"},
            {"word": "はいります I ［だいがくに〜］ (入ります)", "meaning": "上〔大學〕", "jisho": "はいる (入る)"},
            {"word": "でます II ［だいがくを〜］ (出ます)", "meaning": "〔大學〕畢業", "jisho": "でる (出る)"},
            {"word": "おします I (押します)", "meaning": "按、壓、推", "jisho": "おす (押す)"},
            {"word": "のみます I (飲みます)", "meaning": "喝、喝酒", "jisho": "のむ (飲む)"},
            {"word": "はじめます II (始めます)", "meaning": "開始", "jisho": "はじめる (始める)"},
            {"word": "けん가くします III (見學します)", "meaning": "參觀", "jisho": "けんがくする (見學する)"},
            {"word": "でんわします III (電話します)", "meaning": "打電話", "jisho": "でんわする (電話する)"},
            {"word": "わかい (若い)", "meaning": "年輕"},
            {"word": "ながい (長い)", "meaning": "長"},
            {"word": "みじかい (短い)", "meaning": "短"},
            {"word": "あかるい (明るい)", "meaning": "明亮"},
            {"word": "くらい (暗い)", "meaning": "昏暗"},
            {"word": "からだ (體)", "meaning": "身體"},
            {"word": "あたま (頭)", "meaning": "頭、頭腦"},
            {"word": "かみ (髪)", "meaning": "頭髮"},
            {"word": "かお (顔)", "meaning": "臉"},
            {"word": "め (目)", "meaning": "眼睛"},
            {"word": "みみ (耳)", "meaning": "耳朵"},
            {"word": "はな (鼻)", "meaning": "鼻子"},
            {"word": "くち (口)", "meaning": "嘴巴"},
            {"word": "は (歯)", "meaning": "牙齒"},
            {"word": "おなか", "meaning": "肚子"},
            {"word": "あし (足)", "meaning": "腳、腿"},
            {"word": "せ (背)", "meaning": "身高"},
            {"word": "サービス", "meaning": "服務"},
            {"word": "ジョギング", "meaning": "慢跑"},
            {"word": "シャワー", "meaning": "淋浴"},
            {"word": "みどり (緑)", "meaning": "綠色、綠意"},
            {"word": "［お］てら (［お］寺)", "meaning": "寺廟"},
            {"word": "じんじゃ (神社)", "meaning": "神社"},
            {"word": "〜ばん (〜番)", "meaning": "〜號"},
            {"word": "どうやって", "meaning": "怎麼〜（詢問行動方法）"},
            {"word": "どの〜", "meaning": "哪個〜（用於有三個以上的東西時）"},
            {"word": "どれ", "meaning": "哪一個（用於有三個以上的東西時）"},
            {"word": "おひきだしですか。 (お引き出しですか。) 【會話】", "meaning": "您要提款嗎？"},
            {"word": "まず 【會話】", "meaning": "首先"},
            {"word": "つぎに (次に) 【會話】", "meaning": "其次"},
            {"word": "キャッシュカード 【會話】", "meaning": "提款卡、金融卡"},
            {"word": "あんしょうばんごう (暗証番号) 【會話】", "meaning": "密碼"},
            {"word": "きんがく (金額) 【會話】", "meaning": "金額"},
            {"word": "かくにん (確認) 【會話】", "meaning": "確認"},
            {"word": "ボタン 【會話】", "meaning": "按鈕、開關"},
            {"word": "すごいですね。 【練習C】", "meaning": "真了不起。／真棒。"},
            {"word": "［いいえ、］まだまだです。 【練習C】", "meaning": "〔不，〕還差得遠。"},
            {"word": "ジェーアール (JR) 【關聯單語】", "meaning": "JR（日本鐵路公司）"},
            {"word": "ゆきまつり (雪祭り) 【關聯單語】", "meaning": "雪之慶典"},
            {"word": "バンドン 【關聯單語】", "meaning": "萬隆（印尼的地名）"},
            {"word": "フランケン 【關聯單語】", "meaning": "法蘭克尼亞（德國的地名）"},
            {"word": "ベラクルス 【關聯單語】", "meaning": "維拉克魯茲（墨西哥的地名）"},
            {"word": "うめだ (梅田) 【關聯單語】", "meaning": "梅田（大阪的地名）"},
            {"word": "だいがくまえ (大學前) 【關聯單語】", "meaning": "大學前（虛構的公車站名）"}
        ],
        "第17課": [
            {"word": "おぼえます II (覚えます)", "meaning": "記住", "jisho": "おぼえる (覚える)"},
            {"word": "わすれます II (忘れます)", "meaning": "忘記", "jisho": "わすれる (忘れる)"},
            {"word": "なくします I", "meaning": "遺失、丟失", "jisho": "なくす"},
            {"word": "はらいます I (払います)", "meaning": "支付、付款", "jisho": "はらう (払う)"},
            {"word": "かえします I (返します)", "meaning": "歸還、退回", "jisho": "かえす (返す)"},
            {"word": "でかけます II (出かけます)", "meaning": "出門、外出", "jisho": "でかける (出かける)"},
            {"word": "ぬぎます I (脫ぎます)", "meaning": "脫（衣服、鞋等）", "jisho": "ぬぐ (脫ぐ)"},
            {"word": "もって いきます I (持って 行きます)", "meaning": "帶、拿去", "jisho": "もって いく (持って 行く)"},
            {"word": "もって きます III (持って 來ます)", "meaning": "帶、拿來", "jisho": "もって くる (持って 來る)"},
            {"word": "しんぱいします III (心配します)", "meaning": "擔心", "jisho": "しんぱいする (心配する)"},
            {"word": "ざんぎょうします III (殘業します)", "meaning": "加班", "jisho": "ざんぎょうする (殘業する)"},
            {"word": "しゅっちょうします III (出張します)", "meaning": "出差", "jisho": "しゅっちょうする (出張する)"},
            {"word": "のみます I ［くすりを〜］ (飲みます)", "meaning": "吃〔藥〕", "jisho": "のむ (飲む)"},
            {"word": "はいります I ［おふろに〜］ (入ります)", "meaning": "泡（澡）、入浴", "jisho": "はいる (入る)"},
            {"word": "たいせつ［な］ (大切［な］)", "meaning": "重要"},
            {"word": "だいじょうぶ［な］ (大丈夫［な］)", "meaning": "沒問題"},
            {"word": "あぶない (危ない)", "meaning": "危險"},
            {"word": "きんえん (禁菸)", "meaning": "禁菸"},
            {"word": "［けんこう］ほけんしょう (［健康］保険証)", "meaning": "健保卡"},
            {"word": "ねつ (熱)", "meaning": "發燒"},
            {"word": "びょうき (病気)", "meaning": "疾病"},
            {"word": "くすり (薬)", "meaning": "藥"},
            {"word": "［お］ふろ", "meaning": "泡澡、澡盆"},
            {"word": "うわぎ (上著)", "meaning": "上衣、外套"},
            {"word": "したぎ (下著)", "meaning": "內衣褲"},
            {"word": "２、３にち (２、３日)", "meaning": "兩三天"},
            {"word": "２、３〜", "meaning": "兩三〜"},
            {"word": "〜までに", "meaning": "到〜為止（表示時間的期限）"},
            {"word": "ですから", "meaning": "因此"},
            {"word": "どう しましたか。 【會話】", "meaning": "怎麼了嗎？"},
            {"word": "のど 【會話】", "meaning": "喉嚨"},
            {"word": "［〜が］いたいです。 (［〜が］痛いです。) 【會話】", "meaning": "〔〜〕痛。"},
            {"word": "かぜ 【會話】", "meaning": "感冒"},
            {"word": "それから 【會話】", "meaning": "還有"},
            {"word": "おだいじに。 (お大事に。) 【會話】", "meaning": "請多保重。"}
        ],
        "第18課": [
            {"word": "できます II", "meaning": "能夠、會、可以", "jisho": "できる"},
            {"word": "あらいます I (洗います)", "meaning": "洗", "jisho": "あらう (洗う)"},
            {"word": "ひきます I (弾きます)", "meaning": "彈奏（鋼琴等）", "jisho": "ひく (弾く)"},
            {"word": "うたいます I (歌います)", "meaning": "唱歌", "jisho": "うたう (歌う)"},
            {"word": "あつめます II (集めます)", "meaning": "收集、收藏", "jisho": "あつめる (集める)"},
            {"word": "すてます II (捨てます)", "meaning": "丟掉、捨棄", "jisho": "すてる (捨てる)"},
            {"word": "かえます II (換えます)", "meaning": "換", "jisho": "かえる (換える)"},
            {"word": "うんてんします III (運転します)", "meaning": "駕駛", "jisho": "うんてんする (運転する)"},
            {"word": "よやくします III (予約します)", "meaning": "預約、預訂", "jisho": "よやくする (予約する)"},
            {"word": "ピアノ", "meaning": "鋼琴"},
            {"word": "〜メートル", "meaning": "〜公尺"},
            {"word": "げんきん (現金)", "meaning": "現金"},
            {"word": "しゅみ (趣味)", "meaning": "興趣、嗜好"},
            {"word": "にっき (日記)", "meaning": "日記"},
            {"word": "おいのり (お祈り)", "meaning": "祈禱"},
            {"word": "かちょう (課長)", "meaning": "課長、科長"},
            {"word": "ぶちょう (部長)", "meaning": "經理"},
            {"word": "しゃちょう (社長)", "meaning": "總經理、老闆"},
            {"word": "どうぶつ (動物)", "meaning": "動物"},
            {"word": "うま (馬)", "meaning": "馬"},
            {"word": "インターネット", "meaning": "網際網路"},
            {"word": "とくに (特に) 【會話】", "meaning": "特別"},
            {"word": "へえ 【會話】", "meaning": "哦"},
            {"word": "それは おもしろいですね。 【會話】", "meaning": "那一定很有意思。"},
            {"word": "なかなか 【會話】", "meaning": "不輕易、不容易、不簡單"},
            {"word": "ほんとうですか。 【會話】", "meaning": "真的嗎？"},
            {"word": "ぜひ 【會話】", "meaning": "務必"},
            {"word": "ふるさと (故郷) 【關聯單語】", "meaning": "故鄉、家鄉"},
            {"word": "ビートルズ 【關聯單語】", "meaning": "披頭四"},
            {"word": "あきはばら (秋葉原) 【關聯單語】", "meaning": "秋葉原"}
        ],
        "第19課": [
            {"word": "のぼります I (登ります、上ります)", "meaning": "登、上", "jisho": "のぼる (登る、上る)"},
            {"word": "とまります I ［ホテルに〜］ (泊まります)", "meaning": "住〔飯店〕", "jisho": "とまる (泊まる)"},
            {"word": "そうじします III (掃除します)", "meaning": "打掃", "jisho": "そうじする (掃除する)"},
            {"word": "せんたくします III (洗濯します)", "meaning": "洗衣服", "jisho": "せんたくする (洗濯する)"},
            {"word": "なります I", "meaning": "變成、成為", "jisho": "なる"},
            {"word": "ねむい (眠い)", "meaning": "睏"},
            {"word": "つよい (強い)", "meaning": "強"},
            {"word": "よわい (弱い)", "meaning": "弱"},
            {"word": "れんしゅう (練習)", "meaning": "練習"},
            {"word": "ゴルフ", "meaning": "高爾夫"},
            {"word": "すもう (相撲)", "meaning": "相撲"},
            {"word": "おちゃ (お茶)", "meaning": "茶、茶道"},
            {"word": "ひ (日)", "meaning": "日、日子"},
            {"word": "ちょうし (調子)", "meaning": "情形、狀況"},
            {"word": "いちど (一度)", "meaning": "一次"},
            {"word": "いちども (一度も)", "meaning": "連一次也"},
            {"word": "だんだん", "meaning": "漸漸、逐漸"},
            {"word": "進み (もうすぐ)", "meaning": "馬上、即將", "jisho": "もうすぐ"},
            {"word": "おかげさまで", "meaning": "託您的福"},
            {"word": "でも", "meaning": "可是、但是、不過"},
            {"word": "かんぱい (乾杯) 【會話】", "meaning": "乾杯"},
            {"word": "ダイエット 【會話】", "meaning": "減肥"},
            {"word": "むり［な］ (無理［な］) 【會話】", "meaning": "勉強"},
            {"word": "からだに いい (體に いい) 【會話】", "meaning": "對身體好的"},
            {"word": "とうきょうスカイツリー (東京スカイツリー) 【關聯單語】", "meaning": "晴空塔"},
            {"word": "かつしかほくさい (葛飾北齋) 【關聯單語】", "meaning": "葛飾北齋"}
        ]
    }

# --- 2. 側邊欄：功能切換與設定 ---
st.sidebar.header("🎯 選擇學習計畫")
app_mode = st.sidebar.radio("請選擇模式：", ["📖 單字複習 (背單字)", "📝 測驗考試 (刷題)"])

st.sidebar.write("---")
st.sidebar.header("📚 選擇範圍")
lesson_options = list(st.session_state.vocab_data.keys())
lesson_choice = st.sidebar.selectbox("你要複習/測驗哪一課？", ["混合模式 (全部)"] + lesson_options)

if lesson_choice == "混合模式 (全部)":
    raw_pool = []
    for words in st.session_state.vocab_data.values():
        raw_pool.extend(words)
else:
    raw_pool = st.session_state.vocab_data[lesson_choice].copy()

# --- 3. 模式 A：📖 單字複習 (背單字) ---
if app_mode == "📖 單字複習 (背單字)":
    st.title("📖 單字複習區")
    st.markdown(f"**目前範圍：{lesson_choice}**")
    
    display_data = []
    for w in raw_pool:
        display_data.append({
            "日文 (含辭書形標記)": w["word"],
            "辭書形": w.get("jisho", ""),
            "中文解釋": w["meaning"]
        })
        
    df = pd.DataFrame(display_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

# --- 4. 模式 B：📝 測驗考試 (刷題) ---
elif app_mode == "📝 測驗考試 (刷題)":
    st.title("📝 通勤刷題神器")
    
    test_target = st.sidebar.radio("測驗內容：", ["一般中文/日文測驗", "專攻動詞辭書形"])
    test_mode = st.sidebar.radio("題型選擇：", ["手寫/回想題 (中翻日)", "選擇題 (日翻中)"])
    
    if test_target == "專攻動詞辭書形":
        filtered_pool = [w for w in raw_pool if "jisho" in w and w["jisho"]]
    else:
        filtered_pool = raw_pool.copy()

    state_key = f"{lesson_choice}_{test_target}_{test_mode}"
    if "current_test_pool" not in st.session_state or st.session_state.get('last_state') != state_key:
        random.shuffle(filtered_pool)
        st.session_state.current_test_pool = filtered_pool
        st.session_state.current_idx = 0
        st.session_state.last_state = state_key
        st.session_state.show_answer = False
        st.session_state.answered_correctly = None

    test_pool = st.session_state.current_test_pool

    if not test_pool:
        st.warning("⚠️ 這個範圍沒有符合條件的單字喔！")
        st.stop()

    if st.session_state.current_idx >= len(test_pool):
        st.success("🎉 太棒了！全部題目都考完囉！")
        if st.button("🔄 重新挑戰", use_container_width=True):
            st.session_state.current_idx = 0
            random.shuffle(st.session_state.current_test_pool)
            st.rerun()
        st.stop()

    current_word = test_pool[st.session_state.current_idx]
    
    st.progress((st.session_state.current_idx) / len(test_pool))
    st.caption(f"進度: {st.session_state.current_idx + 1} / {len(test_pool)}")

    st.markdown("---")

    # --- 邏輯判斷：手寫/回想題 (中翻日) ---
    if test_mode == "手寫/回想題 (中翻日)":
        # 顯示中文當題目
        st.markdown(f"<h3 style='text-align: center; color: gray;'>請回想日文單字：</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; font-size: 2.8rem;'>{current_word['meaning']}</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        if st.session_state.show_answer:
            # 答案顯示日文與辭書形
            st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>{current_word['word']}</h2>", unsafe_allow_html=True)
            if "jisho" in current_word:
                st.markdown(f"<p style='text-align: center; font-size: 1.5rem;'>辭書形：{current_word['jisho']}</p>", unsafe_allow_html=True)
            
            st.write("<br>", unsafe_allow_html=True)
            if st.button("⏭️ 下一題", use_container_width=True):
                st.session_state.current_idx += 1
                st.session_state.show_answer = False
                st.rerun()
        else:
            if st.button("👀 看答案", use_container_width=True):
                st.session_state.show_answer = True
                st.rerun()

    # --- 邏輯判斷：選擇題 (日翻中) ---
    elif test_mode == "選擇題 (日翻中)":
        # 顯示日文當題目
        st.markdown(f"<h3 style='text-align: center; color: gray;'>這單字是什麼意思？</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; font-size: 2.8rem;'>{current_word['word']}</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        correct_answer = current_word["jisho"] if test_target == "專攻動詞辭書形" else current_word["meaning"]

        if "options" not in st.session_state or st.session_state.get('q_idx_for_options') != st.session_state.current_idx:
            if test_target == "專攻動詞辭書形":
                all_possible = [w["jisho"] for w in test_pool if w["jisho"] != correct_answer]
            else:
                all_possible = [w["meaning"] for w in test_pool if w["meaning"] != correct_answer]
            
            while len(all_possible) < 3:
                all_possible.append(f"隨機選項_{random.randint(1, 99)}")
            
            options = random.sample(all_possible, 3) + [correct_answer]
            random.shuffle(options)
            st.session_state.options = options
            st.session_state.q_idx_for_options = st.session_state.current_idx
            st.session_state.answered_correctly = None

        for opt in st.session_state.options:
            if st.button(opt, use_container_width=True):
                st.session_state.answered_correctly = (opt == correct_answer)

        if st.session_state.answered_correctly is True:
            st.success("✅ 答對了！")
            if st.button("⏭️ 下一題", use_container_width=True):
                st.session_state.current_idx += 1
                st.session_state.answered_correctly = None
                st.rerun()
        elif st.session_state.answered_correctly is False:
            st.error(f"❌ 答錯囉！正確答案是：**{correct_answer}**")
            if st.button("⏭️ 下一題", use_container_width=True):
                st.session_state.current_idx += 1
                st.session_state.answered_correctly = None
                st.rerun()
