import streamlit as st
import random
import pandas as pd
import re

# --- 網頁基本設定 ---
st.set_page_config(page_title="日文單字全攻略 (14-19課)", layout="centered")

# --- 1. 史上最完整單字資料庫 (第14-19課) ---
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
            {"word": "よびます I (呼びます)", "meaning": "叫 (タクシーをよびます)", "jisho": "よぶ (呼ぶ)"},
            {"word": "はなします I (話します)", "meaning": "說", "jisho": "はなす (話す)"},
            {"word": "つかいます I (使います)", "meaning": "使用", "jisho": "つかう (使う)"},
            {"word": "とめます II (止めます)", "meaning": "停止", "jisho": "とめる (止める)"},
            {"word": "みせます II (見せます)", "meaning": "出示、給～人看", "jisho": "みせる (見せる)"},
            {"word": "おしえます II ［じゅうしょを～］ (教えます ［住所を～］)", "meaning": "告訴〔地址〕、教", "jisho": "おしえる (教える)"},
            {"word": "すわります I (座ります)", "meaning": "坐", "jisho": "すわる (座る)"},
            {"word": "たちます I (立ちます)", "meaning": "站立", "jisho": "たつ (立つ)"},
            {"word": "はいります I ［きっさてんに～］ (入ります ［喫茶店に～］)", "meaning": "進入〔咖啡店〕", "jisho": "はいる (入る)"},
            {"word": "でます II ［きっさてんを～］ (出ます ［喫茶店を～］)", "meaning": "離開〔咖啡店〕", "jisho": "でる (出る)"},
            {"word": "ふります I ［あめが～］ (降ります ［雨が～］)", "meaning": "下〔雨〕", "jisho": "ふる (降る)"},
            {"word": "コピーします III", "meaning": "影印", "jisho": "コピーする"},
            {"word": "でんき (電気)", "meaning": "電燈、電氣", "jisho": ""},
            {"word": "エアコン", "meaning": "空調", "jisho": ""},
            {"word": "パスポート", "meaning": "護照", "jisho": ""},
            {"word": "なまえ (名前)", "meaning": "姓名", "jisho": ""},
            {"word": "じゅうしょ (住所)", "meaning": "地址", "jisho": ""},
            {"word": "ちず (地図)", "meaning": "地圖", "jisho": ""},
            {"word": "しお (塩)", "meaning": "鹽", "jisho": ""},
            {"word": "さとう (砂糖)", "meaning": "砂糖", "jisho": ""},
            {"word": "もんだい (問題)", "meaning": "問題", "jisho": ""},
            {"word": "こたえ (答え)", "meaning": "回答、解答", "jisho": ""},
            {"word": "よみかた (読み方)", "meaning": "讀法、唸法", "jisho": ""},
            {"word": "～かた (～方)", "meaning": "～的方法、～的方式", "jisho": ""},
            {"word": "まっすぐ", "meaning": "直直地", "jisho": ""},
            {"word": "ゆっくり", "meaning": "慢慢地、好好地", "jisho": ""},
            {"word": "すぐ", "meaning": "馬上", "jisho": ""},
            {"word": "また", "meaning": "再", "jisho": ""},
            {"word": "あとで", "meaning": "等一下、稍候", "jisho": ""},
            {"word": "もう すこし (もう 少し)", "meaning": "再～一點", "jisho": ""},
            {"word": "もう ～", "meaning": "再～", "jisho": ""},
            {"word": "信号を右へ曲がってください。 【會話】", "meaning": "請在紅綠燈處右轉。", "jisho": ""},
            {"word": "これでお願いします。 【會話】", "meaning": "我用這個付錢。", "jisho": ""},
            {"word": "おつり (お釣り) 【會話】", "meaning": "零錢", "jisho": ""},
            {"word": "さあ 【練習C】", "meaning": "那麼（用於提議、催促做某事時）", "jisho": ""},
            {"word": "あれ？ 【練習C】", "meaning": "咦？（用於感到驚訝、不可思議時）", "jisho": ""},
            {"word": "みどりちょう (みどり町) 【關聯】", "meaning": "綠町（虛構的町名）", "jisho": ""}
        ],
        "第15課": [
            {"word": "おきます I (置きます)", "meaning": "放置", "jisho": "おく (置く)"},
            {"word": "つくります I (作ります、造ります)", "meaning": "做、製造", "jisho": "つくる (作る、造る)"},
            {"word": "うります I (売ります)", "meaning": "賣", "jisho": "うる (売る)"},
            {"word": "しります I (知ります)", "meaning": "知道", "jisho": "しる (知る)"},
            {"word": "すみます I (住みます)", "meaning": "居住", "jisho": "すむ (住む)"},
            {"word": "けんきゅうします III (研究します)", "meaning": "研究", "jisho": "けんきゅうする (研究する)"},
            {"word": "しりょう (資料)", "meaning": "資料", "jisho": ""},
            {"word": "カタログ", "meaning": "目錄、型錄", "jisho": ""},
            {"word": "じこくひょう (時刻表)", "meaning": "時刻表", "jisho": ""},
            {"word": "ふく (服)", "meaning": "衣服", "jisho": ""},
            {"word": "せいひん (製品)", "meaning": "產品", "jisho": ""},
            {"word": "ソフト", "meaning": "軟體", "jisho": ""},
            {"word": "てんしじしょ (電子辞書)", "meaning": "電子辭典", "jisho": ""},
            {"word": "けいざい (経済)", "meaning": "經濟", "jisho": ""},
            {"word": "しやくしょ (市役所)", "meaning": "市政府、市公所", "jisho": ""},
            {"word": "こうこう (高校)", "meaning": "高中", "jisho": ""},
            {"word": "はいしゃ (歯医者)", "meaning": "牙醫", "jisho": ""},
            {"word": "どくしん (独身)", "meaning": "單身、未婚", "jisho": ""},
            {"word": "すみません", "meaning": "對不起、抱歉", "jisho": ""},
            {"word": "おもいだします I (思い出します) 【會話】", "meaning": "想起", "jisho": "おもいだす (思い出す)"},
            {"word": "いらっしゃいます I 【會話】", "meaning": "有、在（「います」的尊敬語）", "jisho": "いらっしゃる"},
            {"word": "みなさん (皆さん) 【練習C】", "meaning": "各位", "jisho": ""},
            {"word": "にっぽんばし (日本橋) 【關聯】", "meaning": "日本橋（大阪的商業區）", "jisho": ""},
            {"word": "みんなのインタビュー 【關聯】", "meaning": "大家的採訪（虛構的電視節目名）", "jisho": ""}
        ],
        "第16課": [
            {"word": "のります I ［でんしゃに～］ (乗ります)", "meaning": "坐、搭乘〔電車〕", "jisho": "のる (乗る)"},
            {"word": "おります II ［でんしゃを～］ (降ります)", "meaning": "下〔電車〕", "jisho": "おりる (降りる)"},
            {"word": "のりかえます II (乗り換えます)", "meaning": "轉乘、換車", "jisho": "のりかえる (乗り換える)"},
            {"word": "あびます II ［シャワーを～］ (浴びます)", "meaning": "淋〔浴〕", "jisho": "あびる (浴びる)"},
            {"word": "いれます II (入れます)", "meaning": "放入、插入", "jisho": "いれる (入れる)"},
            {"word": "だします I (出します)", "meaning": "拿出、取出、提交", "jisho": "だす (出す)"},
            {"word": "おろします I ［おかねを～］ (下ろします)", "meaning": "領〔錢〕", "jisho": "おろす (下ろす)"},
            {"word": "はいります I ［だいがくに～］ (入ります)", "meaning": "上〔大學〕", "jisho": "はいる (入る)"},
            {"word": "でます II ［だいがくを～］ (出ます)", "meaning": "〔大學〕畢業", "jisho": "でる (出る)"},
            {"word": "おします I (押します)", "meaning": "按、壓、推", "jisho": "おす (押す)"},
            {"word": "のみます I (飲みます)", "meaning": "喝、喝酒", "jisho": "のむ (飲む)"},
            {"word": "はじめます II (始めます)", "meaning": "開始", "jisho": "はじめる (始める)"},
            {"word": "けんがくします III (見学します)", "meaning": "參觀", "jisho": "けんがくする (見学する)"},
            {"word": "でんわします III (電話します)", "meaning": "打電話", "jisho": "でんわする (電話する)"},
            {"word": "わかい (若い)", "meaning": "年輕", "jisho": ""},
            {"word": "ながい (長い)", "meaning": "長", "jisho": ""},
            {"word": "みじかい (短い)", "meaning": "短", "jisho": ""},
            {"word": "あかるい (明るい)", "meaning": "明亮", "jisho": ""},
            {"word": "くらい (暗い)", "meaning": "昏暗", "jisho": ""},
            {"word": "からだ (体)", "meaning": "身體", "jisho": ""},
            {"word": "あたま (頭)", "meaning": "頭、頭腦", "jisho": ""},
            {"word": "かみ (髪)", "meaning": "頭髮", "jisho": ""},
            {"word": "かお (顔)", "meaning": "臉", "jisho": ""},
            {"word": "め (目)", "meaning": "眼睛", "jisho": ""},
            {"word": "みみ (耳)", "meaning": "耳朵", "jisho": ""},
            {"word": "はな (鼻)", "meaning": "鼻子", "jisho": ""},
            {"word": "くち (口)", "meaning": "嘴巴", "jisho": ""},
            {"word": "は (歯)", "meaning": "牙齒", "jisho": ""},
            {"word": "おなか", "meaning": "肚子", "jisho": ""},
            {"word": "あし (足)", "meaning": "腳、腿", "jisho": ""},
            {"word": "せ (背)", "meaning": "身高", "jisho": ""},
            {"word": "サービス", "meaning": "服務", "jisho": ""},
            {"word": "ジョギング", "meaning": "慢跑 (～を します：慢跑)", "jisho": ""},
            {"word": "シャワー", "meaning": "淋浴", "jisho": ""},
            {"word": "みどり (緑)", "meaning": "綠色、綠意", "jisho": ""},
            {"word": "［お］てら (［お］寺)", "meaning": "寺廟", "jisho": ""},
            {"word": "じんじゃ (神社)", "meaning": "神社", "jisho": ""},
            {"word": "～ばん (～番)", "meaning": "～號", "jisho": ""},
            {"word": "どうやって", "meaning": "怎麼～ (詢問行動方法)", "jisho": ""},
            {"word": "どの～", "meaning": "哪個～ (用於有三個以上的東西時)", "jisho": ""},
            {"word": "どれ", "meaning": "哪一個 (用於有三個以上的東西時)", "jisho": ""},
            {"word": "お引き出しですか。 【會話】", "meaning": "您要提款嗎？", "jisho": ""},
            {"word": "まず 【會話】", "meaning": "首先", "jisho": ""},
            {"word": "次に 【會話】", "meaning": "其次", "jisho": ""},
            {"word": "キャッシュカード 【會話】", "meaning": "提款卡、金融卡", "jisho": ""},
            {"word": "暗証番号 【會話】", "meaning": "密碼", "jisho": ""},
            {"word": "金額 【會話】", "meaning": "金額", "jisho": ""},
            {"word": "確認 【會話】", "meaning": "確認 (～します：確認)", "jisho": ""},
            {"word": "ボタン 【會話】", "meaning": "按鈕、開關", "jisho": ""},
            {"word": "すごいですね。 【練習C】", "meaning": "真了不起。／真棒。", "jisho": ""},
            {"word": "［いいえ、］まだまだです。 【練習C】", "meaning": "〔不，〕還差得遠。", "jisho": ""},
            {"word": "JR 【關聯】", "meaning": "JR (日本鐵路公司)", "jisho": ""},
            {"word": "雪祭り 【關聯】", "meaning": "雪之慶典", "jisho": ""},
            {"word": "梅田 (大阪的地名) 【關聯】", "meaning": "梅田 (大阪的地名)", "jisho": ""},
            {"word": "大学前 【關聯】", "meaning": "大學前 (虛構的公車站名)", "jisho": ""}
        ],
        "第17課": [
            {"word": "おぼえます II (覚えます)", "meaning": "記住", "jisho": "おぼえる (覚える)"},
            {"word": "わすれます II (忘れます)", "meaning": "忘記", "jisho": "わすれる (忘れる)"},
            {"word": "なくします I", "meaning": "遺失、丟失", "jisho": "なくす"},
            {"word": "はらいます I (払います)", "meaning": "支付、付款", "jisho": "はらう (払う)"},
            {"word": "かえします I (返します)", "meaning": "歸還、退回", "jisho": "かえす (返す)"},
            {"word": "でかけます II (出かけます)", "meaning": "出門、外出", "jisho": "でかける (出かける)"},
            {"word": "ぬぎます I (脱ぎます)", "meaning": "脫（衣服、鞋等）", "jisho": "ぬぐ (脱ぐ)"},
            {"word": "もって 行きます I (持って 行きます)", "meaning": "帶、拿去", "jisho": "もって いく (持って 行く)"},
            {"word": "もって 来ます III (持って 来ます)", "meaning": "帶、拿來", "jisho": "もって くる (持って 来る)"},
            {"word": "しんぱいします III (心配します)", "meaning": "擔心", "jisho": "しんぱいする (心配する)"},
            {"word": "ざんぎょうします III (残業します)", "meaning": "加班", "jisho": "ざんぎょうする (残業する)"},
            {"word": "しゅっちょうします III (出張します)", "meaning": "出差", "jisho": "しゅっちょうする (出張する)"},
            {"word": "のみます I ［くすりを～］ (飲みます ［薬を～］)", "meaning": "吃〔藥〕", "jisho": "のむ (飲む)"},
            {"word": "はいります I ［おふろに～］ (入ります ［お風呂に～］)", "meaning": "泡（澡）、入浴", "jisho": "はいる (入る)"},
            {"word": "たいせつ［な］ (大切［な］)", "meaning": "重要", "jisho": ""},
            {"word": "だいじょうぶ［な］ (大丈夫［な］)", "meaning": "沒問題", "jisho": ""},
            {"word": "あぶない (危ない)", "meaning": "危險", "jisho": ""},
            {"word": "きんえん (禁煙)", "meaning": "禁菸", "jisho": ""},
            {"word": "［健康］保険証", "meaning": "健保卡", "jisho": ""},
            {"word": "ねつ (熱)", "meaning": "發燒", "jisho": ""},
            {"word": "びょうき (病気)", "meaning": "疾病", "jisho": ""},
            {"word": "くすり (薬)", "meaning": "藥", "jisho": ""},
            {"word": "［お］ふろ", "meaning": "泡澡、澡盆", "jisho": ""},
            {"word": "うわぎ (上着)", "meaning": "上衣、外套", "jisho": ""},
            {"word": "したぎ (下着)", "meaning": "內衣褲", "jisho": ""},
            {"word": "２、３にち (２、３日)", "meaning": "兩三天", "jisho": ""},
            {"word": "２、３～", "meaning": "兩三～", "jisho": ""},
            {"word": "～までに", "meaning": "到～為止 (表示時間的期限)", "jisho": ""},
            {"word": "ですから", "meaning": "因此", "jisho": ""},
            {"word": "どう しましたか。 【會話】", "meaning": "怎麼了嗎？", "jisho": ""},
            {"word": "のど 【會話】", "meaning": "喉嚨", "jisho": ""},
            {"word": "［～が］痛いです。 【會話】", "meaning": "〔～〕痛。", "jisho": ""},
            {"word": "かぜ 【會話】", "meaning": "感冒", "jisho": ""},
            {"word": "それから 【會話】", "meaning": "還有", "jisho": ""},
            {"word": "お大事に。 【會話】", "meaning": "請多保重。(對生病、受傷的人所說的話)", "jisho": ""}
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
            {"word": "ピアノ", "meaning": "鋼琴", "jisho": ""},
            {"word": "～メートル", "meaning": "～公尺", "jisho": ""},
            {"word": "げんきん (現金)", "meaning": "現金", "jisho": ""},
            {"word": "しゅみ (趣味)", "meaning": "興趣、嗜好", "jisho": ""},
            {"word": "にっき (日記)", "meaning": "日記", "jisho": ""},
            {"word": "おいのり (お祈り)", "meaning": "祈禱 (～を します：祈禱)", "jisho": ""},
            {"word": "かちょう (課長)", "meaning": "課長、科長", "jisho": ""},
            {"word": "ぶちょう (部長)", "meaning": "經理", "jisho": ""},
            {"word": "しゃちょう (社長)", "meaning": "總經理、老闆", "jisho": ""},
            {"word": "どうぶつ (動物)", "meaning": "動物", "jisho": ""},
            {"word": "うま (馬)", "meaning": "馬", "jisho": ""},
            {"word": "インターネット", "meaning": "網際網路", "jisho": ""},
            {"word": "特に 【會話】", "meaning": "特別", "jisho": ""},
            {"word": "へえ 【會話】", "meaning": "哦 (用於表示欽佩、驚訝時)", "jisho": ""},
            {"word": "それは おもしろいですね。 【會話】", "meaning": "那一定很有意思。", "jisho": ""},
            {"word": "なかなか 【會話】", "meaning": "不輕易、不容易、不簡單 (後接否定)", "jisho": ""},
            {"word": "ほんとうですか。 【會話】", "meaning": "真的嗎？", "jisho": ""},
            {"word": "ぜひ 【會話】", "meaning": "務必", "jisho": ""},
            {"word": "故郷 【關聯】", "meaning": "故鄉、家鄉", "jisho": ""},
            {"word": "ビートルズ 【關聯】", "meaning": "披頭四 (英國著名的樂團)", "jisho": ""},
            {"word": "あきはばら (秋葉原) 【關聯】", "meaning": "秋葉原 (東京的地名)", "jisho": ""}
        ],
        "第19課": [
            {"word": "のぼります I (登ります、上ります)", "meaning": "登、上", "jisho": "のぼる (登る、上る)"},
            {"word": "とまります I ［ホテルに～］ (泊まります)", "meaning": "住〔飯店〕", "jisho": "とまる (泊まる)"},
            {"word": "そうじします III (掃除します)", "meaning": "打掃", "jisho": "そうじする (掃除する)"},
            {"word": "せんたくします III (洗濯します)", "meaning": "洗衣服", "jisho": "せんたくする (洗濯する)"},
            {"word": "なります I", "meaning": "變成、成為", "jisho": "なる"},
            {"word": "ねむい (眠い)", "meaning": "睏", "jisho": ""},
            {"word": "つよい (強い)", "meaning": "強", "jisho": ""},
            {"word": "よわい (弱い)", "meaning": "弱", "jisho": ""},
            {"word": "れんしゅう (練習)", "meaning": "練習 (～を します：練習)", "jisho": ""},
            {"word": "ゴルフ", "meaning": "高爾夫 (～を します：打高爾夫)", "jisho": ""},
            {"word": "すもう (相撲)", "meaning": "相撲 (～［を］します：相撲)", "jisho": ""},
            {"word": "おちゃ (お茶)", "meaning": "茶、茶道", "jisho": ""},
            {"word": "ひ (日)", "meaning": "日、日子", "jisho": ""},
            {"word": "ちょうし (調子)", "meaning": "情形、狀況", "jisho": ""},
            {"word": "いちど (一度)", "meaning": "一次", "jisho": ""},
            {"word": "いちども (一度も)", "meaning": "連一次也 (後接否定)", "jisho": ""},
            {"word": "だんだん", "meaning": "漸漸、逐漸", "jisho": ""},
            {"word": "もうすぐ", "meaning": "馬上、即將", "jisho": ""},
            {"word": "おかげさまで", "meaning": "託您的福 (用於得到支援或熱情款待後表示感謝時)", "jisho": ""},
            {"word": "でも", "meaning": "可是、但是、不過", "jisho": ""},
            {"word": "乾杯 【會話】", "meaning": "乾杯", "jisho": ""},
            {"word": "ダイエット 【會話】", "meaning": "減肥 (～を します：減肥)", "jisho": ""},
            {"word": "無理［な］ 【會話】", "meaning": "勉強", "jisho": ""},
            {"word": "体に いい 【會話】", "meaning": "對身體好的", "jisho": ""},
            {"word": "東京スカイツリー 【關聯】", "meaning": "晴空塔 (位於東京的電波塔)", "jisho": ""},
            {"word": "葛飾北斎 【關聯】", "meaning": "葛飾北齋 (江戶時代有名的浮世繪畫家)", "jisho": ""}
        ]
    }

# --- 2. 核心比對邏輯 ---
def check_ans(u_input, correct_w):
    if not u_input: return False
    u_input = u_input.strip()
    # 提取括號內的文字與主文字
    parts = re.findall(r'[^\s\(\)I]+', correct_w)
    return any(u_input == p for p in parts)

# --- 3. 介面與側邊欄 ---
st.sidebar.title("📚 日文刷題神器")
app_mode = st.sidebar.radio("功能切換", ["📖 總單字表", "📝 開始測驗"])
st.sidebar.write("---")
lesson_choice = st.sidebar.selectbox("選擇課程", ["混合模式 (全部)"] + list(st.session_state.vocab_data.keys()))

# 根據選擇載入資料
if lesson_choice == "混合模式 (全部)":
    raw_pool = [w for v in st.session_state.vocab_data.values() for w in v]
else:
    raw_pool = st.session_state.vocab_data[lesson_choice]

# --- 4. 模式：📖 總單字表 ---
if app_mode == "📖 總單字表":
    st.title(f"📖 {lesson_choice} 複習清單")
    st.dataframe(pd.DataFrame(raw_pool), use_container_width=True, hide_index=True)

# --- 5. 模式：📝 開始測驗 ---
elif app_mode == "📝 開始測驗":
    st.title("📝 通勤隨機刷題")
    test_target = st.sidebar.radio("測驗項目", ["全部單字", "專攻辭書形"])
    test_type = st.sidebar.radio("考題類型", ["✍️ 填寫題 (中翻日)", "🧠 回想題 (中翻日)", "🔘 選擇題 (日翻中)"])

    # 過濾題庫
    pool = [w for w in raw_pool if w.get('jisho')] if test_target == "專攻辭書形" else raw_pool

    # 初始化狀態
    key = f"test_{lesson_choice}_{test_target}_{test_type}"
    if "test_pool" not in st.session_state or st.session_state.get('last_key') != key:
        shuffled = pool.copy()
        random.shuffle(shuffled)
        st.session_state.test_pool = shuffled
        st.session_state.idx = 0
        st.session_state.last_key = key
        st.session_state.show_answer = False

    t_pool = st.session_state.test_pool
    if st.session_state.idx >= len(t_pool):
        st.success("🎉 全部考完囉！")
        if st.button("🔄 再考一次"):
            st.session_state.idx = 0
            random.shuffle(st.session_state.test_pool)
            st.rerun()
        st.stop()

    curr = t_pool[st.session_state.idx]
    st.progress(st.session_state.idx / len(t_pool))
    st.markdown("---")

    # A. 填寫題
    if test_type == "✍️ 填寫題 (中翻日)":
        st.subheader(f"題目：{curr['meaning']}")
        ans = st.text_input("請輸入日文答案...", key=f"ans_{st.session_state.idx}")
        if st.button("✅ 檢查答案"):
            target = curr['jisho'] if test_target == "專攻辭書形" else curr['word']
            if check_ans(ans, target):
                st.success(f"答對了！答案是：{target}")
                if st.button("下一題"):
                    st.session_state.idx += 1
                    st.rerun()
            else:
                st.error(f"錯囉！提示：{curr['word']}")

    # B. 回想題
    elif test_type == "🧠 回想題 (中翻日)":
        st.subheader(f"題目：{curr['meaning']}")
        if st.session_state.show_answer:
            st.markdown(f"### 答案：{curr['word']}")
            if curr.get('jisho'): st.write(f"辭書形：{curr['jisho']}")
            if st.button("⏭️ 下一題"):
                st.session_state.idx += 1
                st.session_state.show_answer = False
                st.rerun()
        else:
            if st.button("👀 看答案"):
                st.session_state.show_answer = True
                st.rerun()

    # C. 選擇題
    elif test_type == "🔘 選擇題 (日翻中)":
        st.subheader(f"日文：{curr['word']}")
        correct = curr['jisho'] if test_target == "專攻辭書形" else curr['meaning']
        if "opts" not in st.session_state or st.session_state.get('opt_idx') != st.session_state.idx:
            others = [w['jisho'] if test_target == "專攻辭書形" else w['meaning'] for w in raw_pool if w != curr]
            st.session_state.opts = random.sample(list(set(others)), 3) + [correct]
            random.shuffle(st.session_state.opts)
            st.session_state.opt_idx = st.session_state.idx
        
        for o in st.session_state.opts:
            if st.button(o, use_container_width=True):
                if o == correct:
                    st.success("✅ 正確！")
                    if st.button("下一題"):
                        st.session_state.idx += 1
                        st.rerun()
                else:
                    st.error(f"❌ 錯誤！正確答案是：{correct}")
