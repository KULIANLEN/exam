<template>
	<view>
		<view class="tittle center bold">
			学生免费流量申请表
		</view>

		<view class="time center">
			<view class="bold">
				申请时间：{{date}}
			</view>
		</view>

		<view class="excel-tittle center bold">
			申请人基本信息
		</view>

		<view>
			<!-- 提交键 -->
			<form @submit="formSubmit">
				<uni-collapse>
					<uni-collapse-item title="申请人基本信息" open="true">
						<view class="card">
							<label class="interval bold">
								认证账号：{{id}}
							</label>
						</view>

						<view class="card">
							<label class="interval bold">
								姓名：{{userName}}
							</label>
						</view>

						<view class="card">
							<label class="interval bold">
								性别：{{gender}}
							</label>
						</view>

						<view class="card">
							<label class="interval bold">
								学院：{{department}}
							</label>
						</view>

						<view class="card">
							<label class="interval bold">
								专业：
							</label>
							<input v-model="Project" name="专业" type="text" placeholder="请输入专业" />
						</view>

						<view class="card">
							<label class="interval bold">
								宿舍地址：
							</label>
							<input v-model="dorm" name="宿舍地址" type="text" placeholder="请输入宿舍地址" />
						</view>

						<view class="card">
							<label class="interval bold">
								联系电话：
							</label>
							<input v-model="phonenumber" name="联系电话" type="text" placeholder="请输入联系电话" />
						</view>

						<view class="card">
							<label class="interval bold">
								辅导员姓名：
							</label>
							<input v-model="teacherName" name="辅导员姓名" type="text" placeholder="请输入辅导员姓名" />
						</view>

						<view class="card">
							<label class="interval bold">
								辅导员联系电话：
							</label>
							<input v-model="teacherPhonenumber" name="辅导员联系电话" type="text" placeholder="请输入辅导员联系电话" />
						</view>


						<view class="card">
							<view class="interval bold">
								申请额度：
							</view>
							<radio-group v-model="howMuch" name='额度'  @change="radioChange" class="radio-card">
								<!-- <label>
									<radio value="10G"/><text class = "radio">10G</text>
								</label>
								<label>
									<radio value="30G"/><text class = "radio">30G</text>
								</label>
								<label>
									<radio value="50G"/><text class = "radio">50G</text>
								</label> -->
								<label v-for="(item, index) in items" :key="item.value">
									<view>
										<radio :value="item.value" :checked="index === current" />
									</view>
									<view class = "radio">
										{{item.name}}
									</view>
								</label>
							</radio-group>
						</view>

						<view class="card">
							<label class="interval bold">
								申请原因简述：
							</label>
							<input v-model="reason" name="申请原因简述" type="text" placeholder="请简述申请原因" />
						</view>

						<view class="card">
							<view class="interval bold">
								申请相关附件（非必填）
							</view>
							<uni-section title="选择相关附件" v-model="upload">
								<uni-file-picker file-mediatype="all"  @progress="progress"
									@success="success" @fail="fail" @select="select" /><!-- 各种文件类型 -->
								</uni-file-picker>
							</uni-section>
						</view>
					</uni-collapse-item>
				</uni-collapse>
				
				<view>
					<button form-type="submit">提交</button>
				</view>
			</form>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				id:"",
				userName: "",
				gender: "",
				department: "",
				Project: "",
				dorm: "",
				phonenumber: "",
				teacherName: "",
				teacherPhonenumber: "",
				howMuch: "",
				reason: "",
				upload:"",
				date: new Date().getFullYear() + "-" + (new Date().getMonth()+1) + "-" + new Date().getDate(),
				items: [{
					value: '10G',
					name: '10G'
					},
					{
					value: '30G',
					name: '30G'
					},
					{
					value: '50G',
					name: '50G'
					},
				],
				current: 0
			}
		},
		methods: {
			radioChange: function(evt) {
				for (let i = 0; i < this.items.length; i++) {
					if (this.items[i].value === evt.detail.value) {
						this.current = i;
						break;
					}
				}
			},
			upload() {
				this.$refs.files.upload()
			},
			select(e) { // 获取上传状态
				console.log('选择文件：', e)
			},
			progress(e) { // 获取上传进度
				console.log('上传进度：', e)
			},
			success(e) { // 上传成功
				console.log('上传成功')
			},
			fail(e) { // 上传失败
				console.log('上传失败：', e)
			},
			formSubmit: function(e) { //点击提交按钮后
				var formdata = e.detail.value //字典
				console.log(formdata)
				for (var i in formdata) {//不知道为什么选项打不上去，在这赋一下
					if(formdata[i] =="10G"){
						// console.log(formdata[i])
						this.howMuch = '0'
						break
					} else if(formdata[i] =="30G"){
						// console.log(formdata[i])
						this.howMuch = '1'
						break
					} else if(formdata[i] =="50G"){
						// console.log(formdata[i])
						this.howMuch = '2'
						break
					}
				}
				if(this.Project==""){
					uni.showModal({
						title: '请填写专业~',
						confirmText:"马上去填",
						showCancel: false
						});
				}else if(this.dorm==''){
					uni.showModal({
						title: '请填写宿舍地址~',
						confirmText:"马上去填",
						showCancel: false
						});
				}else if(this.phonenumber==''){
					uni.showModal({
						title: '请填写联系电话~',
						confirmText:"马上去填",
						showCancel: false
						});
				}else if(this.teacherName==''){
					uni.showModal({
						title: '请填写辅导员姓名~',
						confirmText:"马上去填",
						showCancel: false
						});
				}else if(this.teacherPhonenumber==''){
					uni.showModal({
						title: '请填写辅导员联系电话~',
						confirmText:"马上去填",
						showCancel: false
						});
				}else if(this.howMuch==''){
					uni.showModal({
						title: '请选择申请额度~',
						content:"来都来了不申请个50G?✧(≖ ◡ ≖)",
						confirmText:"马上去填",
						showCancel: false
					});
				}else if(this.reason==''){
					uni.showModal({
						title: '请简述申请原因~',
						confirmText:"马上去填",
						showCancel: false
					});
				}else{
					console.log(formdata)
					var list = ""
					for (var i in formdata) {
						list += i + ": " + formdata[i] //显示表单数据
					}
					uni.showModal({
						title: '填写内容：',
						content: list,
						success:(res) => {
							if (res.confirm) {
								console.log('用户点击确定');
								let that = this
								uni.request({
									url: 'http://127.0.0.1:8000/tableSubmit/current',
									method: 'GET',
									data: {
										Project: this.Project,
										dorm: this.dorm,
										phonenumber: this.phonenumber,
										teacherName: this.teacherName,
										teacherPhonenumber: this.teacherPhonenumber,
										howMuch: this.howMuch,
										reason: this.reason,
										upload:this.upload
									},
									success: (res) => {
										if (res.data.status_code == 100) {
											uni.showToast({
												title: '提交成功ヾ(≧▽≦*)o'
											})
										} else {
											console.log(res.data)
											uni.showToast({
												title: '提交失败Σ(°ロ°)',
												comment: '请稍后重试...',
											})
										}
									}
								})
							}else if (res.cancel) {
							console.log('用户点击取消');
							}
						},
						showCancel: true //是否有取消按钮
					});
				}
			},
			getData(){
				let that = this
				uni.request({
					url:'http://127.0.0.1:8000/tableSubmit/fixedInfo',
					method:'GET',
					success:(res) => {
						this.id=res.data.id,
						this.userName=res.data.name,
						this.gender=res.data.gender,
						this.department=res.data.department
					}
				})
			}
		},
		onLoad(res) {
			this.getData();
			let that = this;
			setInterval(function(){
				uni.setStorageSync('name',that.name)
				uni.setStorageSync('gender',that.gender)
				uni.setStorageSync('Project',that.Project)
				uni.setStorageSync('dorm',that.dorm)
				uni.setStorageSync('phonenumber',that.phonenumber)
				uni.setStorageSync('teacherName',that.teacherName)
				uni.setStorageSync('teacherPhonenumber',that.teacherPhonenumber)
				uni.setStorageSync('howMuch',that.howMuch)
				uni.setStorageSync('reason',that.reason)
				uni.setStorageSync('id',that.id)
				uni.setStorageSync('department',that.department)
				uni.setStorageSync('upload',that.upload)
			},2000)
		},
		onShow(res){
		this.getData();
		this.name = uni.getStorageSync('name')
		this.gender = uni.getStorageSync('gender')
		this.Project = uni.getStorageSync('Project')
		this.dorm = uni.getStorageSync('dorm')
		this.phonenumber = uni.getStorageSync('phonenumber')
		this.teacherName = uni.getStorageSync('teacherName')
		this.teacherPhonenumber = uni.getStorageSync('teacherPhonenumber')
		this.howMuch = uni.getStorageSync('howMuch')
		this.reason = uni.getStorageSync('reason')
		this.id = uni.getStorageSync('id')
		this.department = uni.getStorageSync('department')
		this.upload = uni.getStorageSync('upload')
		}
	}
</script>

<style>
	.center {
		display: flex;
		justify-content: center;
		align-items: center;
	},

	.bold {
		font-weight: 700;
	},

	.tittle {
		font-size: larger;
		margin: 8rpx;
	},

	.time {
		font-size: samll;
	},

	.excel-tittle {
		font-size: large;
		margin: 40rpx;
	},

	.interval {
		/* 项目标题和内容间距 */
		margin-bottom: 10rpx;
	},

	.card {
		/* 项目 */
		padding: 20rpx;
		margin-left: 50rpx;
		margin-right: 50rpx;
		margin-bottom: 35rpx;
		background-color: rgba(242, 242, 242, 0.5);
		border-radius: 20rpx;
	},
	.radio-card{
		display: flex;
		flex-wrap: nowrap;
	},
	.radio{
		margin-right: 180rpx;
	}
</style>
